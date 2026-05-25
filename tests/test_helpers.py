import pytest
from utils.helpers import parse_emails, find_user_by_id
from utils.json_helper import load_json, get_nested

USERS = [
    {"id": 1, "email": "alice@mail.com", "active": True},
    {"id": 2, "email": "bob@mail.com",   "active": False},
    {"id": 3, "email": "carol@mail.com", "active": True},
]

def test_parse_emails_returns_only_active():
    result = parse_emails(USERS)
    assert result == ["alice@mail.com", "carol@mail.com"]

def test_find_user_returns_correct_user():
    user = find_user_by_id(USERS, 1)
    assert user["email"] == "alice@mail.com"

def test_find_user_returns_none_if_missing():
    user = find_user_by_id(USERS, 99)
    assert user is None

def test_load_json_returns_dict():
    data = load_json("tests/data/user_response.json")
    assert isinstance(data, dict)
    assert "data" in data

def test_get_nested_returns_value():
    data = load_json("tests/data/user_response.json")
    email = get_nested(data, "data", "email")
    assert email == "janet.weaver@reqres.in"

def test_get_nested_returns_default_if_missing():
    data = load_json("tests/data/user_response.json")
    city = get_nested(data, "data", "address", "city", default="unknown")
    assert city == "unknown"