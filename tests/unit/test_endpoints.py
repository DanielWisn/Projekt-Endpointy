from app import usersController
import json

def get_user(lista:list[dict],key:"str",value:"str") -> dict:
    for i in lista:
        if i[key] == value:
             return i

def test_read_users():
    with open('./app/users.json','r') as f:
            users = json.load(f)

    assert usersController.read_users()[0] == users

def test_read_users_id():
    with open('./app/users.json','r') as f:
            users = json.load(f)
    assert usersController.read_users(2)[0] == get_user(users,"id",2)

def test_add_user():
    usersController.add_user({"name":"Bartosz","lastname":"Cudny"})
    with open('./app/users.json','r') as f:
            users = json.load(f)
    answer = get_user(users,"name","Bartosz")
    assert  None != answer

def test_edit_user():
    usersController.edit_user({"name":"Bartosz","lastname":"Cudny"},4)
    with open('./app/users.json','r') as f:
            users = json.load(f)
    answer = get_user(users,"id",4)
    assert {"name":"Bartosz","lastname":"Cudny","id":4} == answer

def test_edit_user_error_id():
    assert usersController.edit_user({"name":"Bartosz","lastname":"Cudny"},200)[1] == 400

def test_edit_user_error_body():
    assert usersController.edit_user({"error":"error"},2)[1] == 400

def test_put_user():
    usersController.put_user({"name":"Antoni","lastname":"Kmuk"},6)
    with open('./app/users.json','r') as f:
            users = json.load(f)
    answer = get_user(users,"name","Antoni")
    assert {"name":"Antoni","lastname":"Kmuk","id":6} == answer

def test_put_user_edit():
    usersController.put_user({"name":"Antoni","lastname":"Kmuk"},2)
    with open('./app/users.json','r') as f:
            users = json.load(f)
    answer = get_user(users,"id",2)
    assert {"name":"Antoni","lastname":"Kmuk","id":2} == answer

def test_delete_user():
    usersController.delete_user(6)
    with open('./app/users.json','r') as f:
            users = json.load(f)
    answer = get_user(users,"id",6)
    assert None == answer

def test_delete_user_error():
    assert usersController.delete_user(8)[1] == 400