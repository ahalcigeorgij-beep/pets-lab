import json
from exceptions import StorageError


def save_json(data, path):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except OSError as e:
        raise StorageError(f"Ошибка записи: {e}") from e


def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError as e:
        raise StorageError(f"Файл не найден: {path}") from e
    except json.JSONDecodeError as e:
        raise StorageError(f"Плохой JSON: {e}") from e
