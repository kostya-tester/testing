from typing import Optional

def parse_emails(users: list) -> list:
    return [u["email"] for u in users if u.get("active")]

def find_user_by_id(users: list, user_id: int) -> Optional[dict]:
    return next((u for u in users if u["id"] == user_id), None)