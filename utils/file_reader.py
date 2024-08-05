import json
from pathlib import Path

base_path = Path.cwd() / "data"


def read_file(file_name: str) -> dict:
    file_path = get_file_with_json_ext(file_name)
    with open(file_path, mode="r") as file:
        return json.load(file)


def get_file_with_json_ext(file_name: str) -> Path:
    if not file_name.endswith(".json"):
        file_name += ".json"
    return base_path / file_name
