import json
from pathlib import Path
import os


def make_json(path):
    if not Path(path).is_file():
        with open(path, 'w') as f:
            json.dump({}, f)
    return None


def json_update(path, result, keyword):
    with open(path, 'r+') as f:
        data = json.load(f)
        
        if keyword not in data:
            data[keyword] = [result]
        else:
            data[keyword].append(result)
            
        f.seek(0)
        json.dump(data, f)
    return None
