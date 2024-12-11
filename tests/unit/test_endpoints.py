from app import usersController

def test_read_users():
    assert usersController.read_users()[1] == 200

def test_read_users_id():
    assert usersController.read_users(1)[1] == 200

def test_add_user():
    assert usersController.add_user({"name":"Bartosz","lastname":"Cudny"})[1] == 201

def test_edit_user():
    assert usersController.edit_user({"name":"Bartosz","lastname":"Cudny"},4)[1] == 204

def test_edit_user_error_id():
    assert usersController.edit_user({"name":"Bartosz","lastname":"Cudny"},200)[1] == 400

def test_edit_user_error_body():
    assert usersController.edit_user({"error":"error"},2)[1] == 400

def test_put_user():
    assert usersController.put_user({"name":"Antoni","lastname":"Kmuk"},6)[1] == 204

def test_put_user_edit():
    assert usersController.put_user({"name":"Antoni","lastname":"Kmuk"},5)[1] == 204

def test_delete_user():
    assert usersController.delete_user(6)[1] == 204

def test_delete_user_error():
    assert usersController.delete_user(8)[1] == 400