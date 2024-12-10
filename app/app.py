from flask import Flask
from flask import request
from flask.typing import ResponseReturnValue
from app.controllers import usersController

app = Flask(__name__)


@app.get("/users")
def get_users() -> ResponseReturnValue:
    controller = usersController()
    body = controller.read_users()
    return body

@app.get("/users/<int:user_id>")
def get_users_id(user_id:int) -> ResponseReturnValue:
    controller = usersController()
    body = controller.read_users(user_id)
    return body

@app.post("/users")
def post_user() -> ResponseReturnValue:
    controller = usersController()
    user = request.json
    controller.add_user(user) 

@app.patch("/users/<int:user_id>")
def patch_user(user_id:int) -> ResponseReturnValue:
    controller = usersController()
    user = request.json
    if user["lastname"] == None or user["name"] == None:
        return "", 400
    controller.edit_user(user,user_id) 

@app.put("/users/<int:user_id>")
def put_user(user_id:int) -> ResponseReturnValue:
    controller = usersController()
    user = request.json
    controller.put_user(user,user_id)

@app.delete("/users/<int:user_id>")
def delete_user(user_id:int) -> ResponseReturnValue:
    controller = usersController()
    user = request.json
    controller.delete_user(user,user_id)

if __name__ == '__main__':
    app.run()