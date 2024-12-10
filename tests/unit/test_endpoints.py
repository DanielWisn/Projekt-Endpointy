from app.app import app
from app import get_users,get_users_id,post_user,patch_user,put_user,delete_user
from flask import Flask
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_flask_app_exists() -> None:
    assert isinstance(app,Flask)

def test_get_users() -> None:
    with app.test_request_context():
        assert get_users()[1] == 200

def test_get_users_id() -> None:
    with app.test_request_context():
        assert get_users_id(2)[1] == 200

def test_post_user(client) -> None:
    response = client.post("/users", json={"name":"Tymon","lastname":"Gorczyca"})
    assert response.status_code == 201
