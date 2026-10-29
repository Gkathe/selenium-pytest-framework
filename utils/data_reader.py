import json
from pathlib import Path

def load_json(filename):
    path = Path(__file__).parent.parent / "data" / filename
    with open(path, encoding="utf-8") as f:
        return json.load(f)