import json
from typing import Union, Any, Dict, List
from pathlib import Path


def load_txt_list(filename: str) -> List[str]:
    """
    load text file, each line in file as element in a new list.

    Args:
        filename (str): relative path to txt file

    Returns:
        list[str]: return data in txt file
    """
    with open(filename, "r", encoding="UTF-8") as f:
        lines = f.readlines()
    content_list = [line.replace("\n", "") for line in lines]
    return content_list


def load_json(filename: str) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """
    Load json file.

    Args:
        filename (str): relative path to json file

    Returns:
        Union[list[dict[str, Any]], dict[str, Any]]: return data in json file
    """
    with open(filename, "r", encoding="utf-8") as f:
        parsed = json.load(f)

    return parsed

def make_json(path: str, data: Any) -> None:
    if not Path(path).is_file():
        with open(path, 'w') as f:
            json.dump(data, f, encoding="utf-8")
    return None
