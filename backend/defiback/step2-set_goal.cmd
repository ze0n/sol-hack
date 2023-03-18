curl -X POST -H "Content-Type: application/json" -d " { \"userId\": \"16fd2706-8baf-433b-82eb-8c7fada847da\", \"type\": \"steps\", \"goalDetails\": { \"date\": \"2023-03-18\", \"numberOfSteps\": 8000 } }" http://localhost:5000/api/challenges

curl -X GET -H "Content-Type: application/json" -d "" http://localhost:5000/api/challenges