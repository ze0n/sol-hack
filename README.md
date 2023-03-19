# DOOERS

## Structure of the repo

### Frontend

`frontend` - ReactNative application, setting the goal and tracking the number of steps.

### Backend

`backend` - Python Flask application managing the goal mechanics (time, number of steps).

`backend\defiback\start.cmd`

then do steps to simulate a data flow

### Contract

`contract` - Smart contract in Anchor which manages transfers of money. Oracles are not implemented. Idea is that we transfer money from the user's wallet to a manager's account by creating a Goal account. Goal id is then managed by the backend which updates the state by contract's method.