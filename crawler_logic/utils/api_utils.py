import logging
import requests
from typing import Any, Dict
from requests.models import Response


error_logger = logging.getLogger("error_logger")


def send_post_request(headers: dict, url: str, json_body: dict) -> Any:
    res = requests.post(headers=headers, url=url, json=json_body)

    if res.status_code == int(200):
        return res.json()
    else:
        basic_request_assert(res)
        raise RuntimeError(f"Response {res.status_code} from {url} fails.")


def send_get_request(headers: dict, url: str) -> Any:
    res = requests.get(headers=headers, url=url)

    if res.status_code == int(200):
        return res.json()
    else:
        basic_request_assert(res)
        raise RuntimeError(f"Response {res.status_code} from {url} fails.")


def basic_request_assert(res: Response) -> None:
    if res.status_code != 200:
        print("-"*10)
        print(res.text)
        print("="*10)


def send_request(site: str, url: str) -> Dict[str, Any]:
    try:
        if site in ["lazada", "shopee"]:
            headers = {}
        else:
            headers = {
                "User-Agent": "PostmanRuntime/7.29.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }
        return send_get_request(headers, url)
    except RuntimeError as e:
        # error_logger.info(f"Fail to send request to {url}. Error {e}")
        return {}
