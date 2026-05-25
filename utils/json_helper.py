import json
from typing import Any, Optional

def load_json(path: str) -> Any:
    """Загружает JSON из файла."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def get_nested(data: dict, *keys: str, default=None) -> Optional[Any]:
    """Безопасно достаёт вложенное поле.
    Пример: get_nested(data, 'user', 'address', 'city')
    """
    for key in keys:
        if not isinstance(data, dict):
            return default
        data = data.get(key, default)
    return data