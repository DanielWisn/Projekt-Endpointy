from flask import Flask
from flask import jsonify
from flask import request
from flask.typing import ResponseReturnValue
from controllers import usersController

app = Flask(__name__)


@app.get("/users")
def users() -> ResponseReturnValue:
    controller = usersController()
    body = {"ping_id": 200, "ping_message": controller.read_users()}
    return body

@app.get("/users/<int:user_id>")
def users_id(user_id:int) -> ResponseReturnValue:
    controller = usersController()
    body = controller.read_users(user_id)
    return body

@app.post("/users")
def add_user() -> ResponseReturnValue:
    controller = usersController()
    user = request.json
    controller.add_user(user) 

@app.patch("/users/<int:user_id>")
def add_user(user_id:int) -> ResponseReturnValue:
    controller = usersController()
    user = request.json
    if user["lastname"] == None or user["name"] == None:
        return "", 400
    controller.edit_user(user,user_id) 

if __name__ == '__main__':
    app.run()