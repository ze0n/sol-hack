from flask import Flask, render_template, url_for
import json
from flask import Flask, jsonify, request
import datetime
from flask_bootstrap import Bootstrap

app = Flask(__name__)

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
        "status": "Pending",
        "goalDetails": {
            "date": "18/03/2023",
            "numberOfSteps": 5
        }
    }
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()


@app.route('/profile', methods=['POST'])
def create_profile():
    print("Create profile")
    userInfo = request.get_json()
    print(userInfo)
    id = userInfo['id']
    usersDb[id] = userInfo
    return "", 200

@app.route('/challenges', methods=['POST'])
def create_challenge():
    print("Create challenge")
    challengeInfo = request.get_json()
    print(challengeInfo)
    id = challengeInfo['id']
    # 2020-03-20T01:31:12.467113+00:00
    now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
    challengeInfo["createdAt"] = now
    if(id in challengesDb):
        return "Already exists", 500

    challengesDb[id] = challengeInfo
    return "", 204

@app.route('/')
def main():
    print(url_for('list_users'))
    print(url_for('list_challenges'))
    return render_template('main.html')

@app.route('/users')
def list_users():
    for userid in usersDb:
        print(url_for('list_users'))

@app.route('/challenges')
def list_challenges():
    for challengeid in challengesDb:
        print(url_for('list_challenges'))

@app.route('/challenges/<challenge_id>')
def goal_status(challenge_id=None):
    ret = json.dumps()
    return "", 200

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

if(__name__ == "__main__"):
    create_app()