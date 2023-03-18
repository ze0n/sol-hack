from flask import Flask, render_template, url_for
import json
from flask import Flask, jsonify, request
import datetime
from flask_bootstrap import Bootstrap
import uuid

app = Flask(__name__)
Bootstrap(app)

usersDb = {
    "82468723468723": {
        "id": "82468723468723",
        "name": "Alex Brain",
        "password": "kskask",
        "walletid": "823482365783"
    }
}

challengesDb = {
    "8758358232": {
        "id": "8758358232",
        "userId": "82468723468723",
        "type": "steps", 
        "status": "pending",
        "goalDetails": {
            "date": "2023-03-18",
            "numberOfSteps": 5
        }
    }
}

# Helper
def get_user_challenges(userId):
    global usersDb, challengesDb
    return list(filter(lambda x: x["userId"] == userId, challengesDb.values()))

def gen_user_id():
    return '16fd2706-8baf-433b-82eb-8c7fada847da'
    # return f"{uuid.uuid4()}"

def gen_challenge_id():
    return '21fd2706-8baf-433b-82eb-8c7fada847da'
    # return f"{uuid.uuid4()}"

sampleMobileData = {
    "date": "2023-03-18",
    "stepsToday": 4500
}

class StepsGoalImpl:
    goalType = "steps"
    def __init__(self) -> None:
        pass
    
    def evaluateGoalStatus(self, pendingGoalInfo, newUserMobileInfo):
        newStatus = pendingGoalInfo["status"]
        
        print("==================================")
        print(pendingGoalInfo, newUserMobileInfo)
        print("==================================")

        # Still today
        todayUtc = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()[:8]

        if(todayUtc > pendingGoalInfo["goalDetails"]["date"]):
            newStatus = "failed"
        elif(newUserMobileInfo["stepsToday"] >= pendingGoalInfo["goalDetails"]["numberOfSteps"]):
            newStatus = "won"
        
        return newStatus

# API
@app.route('/api/signup', methods=['POST'])
def create_profile():
    global usersDb, challengesDb
    userInfo = request.get_json()
    print(userInfo)
    id = gen_user_id()
    userInfo["id"] = id
    usersDb[id] = userInfo
    print(usersDb)
    return f"{{\"id\": \"{id}\"}}", 200

@app.route('/api/challenges', methods=['POST'])
def create_challenge():
    global usersDb, challengesDb
    challengeInfo = request.get_json()
    print(challengeInfo)
    id = gen_challenge_id()
    challengeInfo['id'] = id
    challengeInfo['status'] = "pending"
    # 2020-03-20T01:31:12.467113+00:00
    now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
    challengeInfo["createdAt"] = now
    if(id in challengesDb):
        return "Already exists", 500

    challengesDb[id] = challengeInfo
    print(challengesDb)
    return f"{{\"id\": \"{id}\"}}", 200

@app.route('/api/challenges/<challenge_id>', methods=['GET'])
def goal_status(challenge_id=None):
    global usersDb, challengesDb
    chInfo = challengesDb[challenge_id]
    ret = {
        "id": chInfo["id"],
        "status": chInfo["status"]
    }
    return json.dumps(ret), 200

@app.route('/api/users/<userId>/data', methods=['POST'])
def push_mobile_data(userId=None):
    global usersDb, challengesDb

    data = request.get_json()

    print(f"Received new data for the user '{userId}': {data}")

    if(userId not in usersDb):
        print(usersDb)
        return f"User {userId} doesn't exist", 404

    userInfo = usersDb[userId]
    
    challenges = get_user_challenges(userId)
    for challenge in challenges:
        challengeId = challenge["id"]
        if(challenge["type"] == "steps"):
            impl = StepsGoalImpl()
            newStatus = impl.evaluateGoalStatus(challenge, data)
            oldStatus = challengesDb[challengeId]["status"]
            if(oldStatus != newStatus):
                challengesDb[challengeId]["status"] = newStatus
                print(f"User's '{userId}' challenge '{challengeId}' status changed from '{oldStatus}' to '{newStatus}'")
        else:
            return "Unknown challenge type", 500
    return "", 200

@app.route('/api/users', methods=['GET'])
def users():
    global usersDb, challengesDb
    return json.dumps(list(usersDb.values()))

@app.route('/api/challenges', methods=['GET'])
def challenges():
    global usersDb, challengesDb
    return json.dumps(list(challengesDb.values()))


# VISIBLE

@app.route('/')
def main():
    global usersDb, challengesDb

    print(url_for('list_users'))
    print(url_for('list_challenges'))
    return render_template('main.html')

@app.route('/users')
def list_users():
    global usersDb, challengesDb
    print(usersDb.values())
    return render_template('users.html', context={"users": list(usersDb.values())})

@app.route('/challenges')
def list_challenges():
    global usersDb, challengesDb
    print(challengesDb.values())
    return render_template('challenges.html', context={"challenges": list(challengesDb.values())})
