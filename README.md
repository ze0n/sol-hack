# DOOERS

## Structure of the repo

### Frontend

`frontend` - ReactNative application, setting the goal and tracking the number of steps.

### Backend

`backend` - Python Flask application managing the goal mechanics (time, number of steps).

```
cd backend\defiback
venv\Scripts\activate
start.cmd
```

then do steps to simulate a data flow

### Contract

`contract` - Smart contract in Anchor which manages transfers of money. Oracles are not implemented. Idea is that we transfer money from the user's wallet to a manager's account by creating a Goal account. Goal id is then managed by the backend which updates the state by contract's method.

![s1](https://github.com/ze0n/sol-hack/blob/main/contract/img/1.jpg?raw=true)
![s2](https://github.com/ze0n/sol-hack/blob/main/contract/img/2.jpg?raw=true)

![s1](/contract/img/1.jpg)
![s2](/contract/img/2.jpg)
