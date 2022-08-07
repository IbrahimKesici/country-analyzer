import json
from pathlib import Path
from typing import Union


def read_json(path:Union[str, Path]) -> dict:
    try:
        with open(path, 'r') as f:
            content = json.load(f)
        return content
    except Exception as e:
        print(e)