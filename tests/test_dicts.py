import pytest
def test_users():
    user = {"id": 1, "email": "a@b.com", "active": True}
    assert "email" in user
def test_use():
    user = {"id": 1, "email": "a@b.com", "active": True}
    assert user["id"] == 1
def test_us():
    user = {"id": 1, "email": "a@b.com", "active": True}
    assert "password" not in user
def test_u():
    user = {"id": 1, "email": "a@b.com", "active": True}
    user["active"] = False
    assert user["active"] == False
def test_u2():
    user = {"id": 1, "email": "a@b.com", "active": True}
    keys = list(user.keys())
    assert keys == ["id", "email", "active"]






