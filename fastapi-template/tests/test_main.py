import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/..'))

import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}


def test_about_route(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert response.json() == {"message": "This is the about page."}


def test_create_user(client):
    user = {"id": 1, "username": "alice", "email": "alice@example.com", "is_active": True}
    response = client.post("/admin/users/", json=user)
    assert response.status_code == 200
    assert response.json()["username"] == "alice"


def test_create_user_already_exists(client):
    user = {"id": 10, "username": "dupe", "email": "dupe@example.com", "is_active": True}
    client.post("/admin/users/", json=user)
    response = client.post("/admin/users/", json=user)
    assert response.status_code == 400
    assert response.json()["detail"] == "User already exists"


def test_get_user_by_id(client):
    user = {"id": 2, "username": "bob", "email": "bob@example.com", "is_active": True}
    client.post("/admin/users/", json=user)
    response = client.get("/admin/users/2")
    assert response.status_code == 200
    assert response.json()["username"] == "bob"


def test_get_user_not_found(client):
    response = client.get("/admin/users/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_get_user_by_username(client):
    user = {"id": 3, "username": "carol", "email": "carol@example.com", "is_active": True}
    client.post("/admin/users/", json=user)
    response = client.get("/admin/users/by-username/carol")
    assert response.status_code == 200
    assert response.json()["email"] == "carol@example.com"


def test_get_user_by_username_not_found(client):
    response = client.get("/admin/users/by-username/doesnotexist")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_update_user(client):
    user = {"id": 4, "username": "dave", "email": "dave@example.com", "is_active": True}
    client.post("/admin/users/", json=user)
    updated = {"id": 4, "username": "davey", "email": "davey@example.com", "is_active": False}
    response = client.put("/admin/users/4", json=updated)
    assert response.status_code == 200
    assert response.json()["username"] == "davey"
    assert response.json()["is_active"] is False


def test_update_user_not_found(client):
    user = {"id": 20, "username": "nouser", "email": "nouser@example.com", "is_active": True}
    response = client.put("/admin/users/20", json=user)
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_delete_user(client):
    user = {"id": 5, "username": "eve", "email": "eve@example.com", "is_active": True}
    client.post("/admin/users/", json=user)
    response = client.delete("/admin/users/5")
    assert response.status_code == 200
    assert response.json()["detail"] == "User deleted"


def test_delete_user_not_found(client):
    response = client.delete("/admin/users/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_list_users(client):
    # Clear and add two users
    client.post("/admin/users/", json={"id": 6, "username": "frank", "email": "frank@example.com", "is_active": True})
    client.post("/admin/users/", json={"id": 7, "username": "grace", "email": "grace@example.com", "is_active": True})
    response = client.get("/admin/users/")
    assert response.status_code == 200
    usernames = [u["username"] for u in response.json()]
    assert "frank" in usernames and "grace" in usernames


def test_add_msg(client):
    response = client.post("/messages/hello/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"]["msg_name"] == "hello"


def test_list_messages(client):
    # Add two messages
    client.post("/messages/first/")
    client.post("/messages/second/")
    response = client.get("/messages")
    assert response.status_code == 200
    data = response.json()
    assert "messages:" in data
    assert any(msg["msg_name"] == "first" for msg in data["messages:"].values())
    assert any(msg["msg_name"] == "second" for msg in data["messages:"].values())


def test_actor_feat_impersonating():
    from main import feat_observer
    result = {}
    context = {"impersonating": True}
    # Simulate the observer notification for the Actor feat
    feat_observer.notify(["Actor"], context, result)
    assert "Deception" in result.get("advantage_checks", [])
    assert "Performance" in result.get("advantage_checks", [])
    assert any("impersonating" in note for note in result.get("notes", []))


def test_actor_feat_not_impersonating():
    from main import feat_observer
    result = {}
    context = {"impersonating": False}
    feat_observer.notify(["Actor"], context, result)
    assert "advantage_checks" not in result or not result["advantage_checks"]
    assert any("not applied" in note for note in result.get("notes", []))
