import logging

from .config import API_LIST, HOT_TREND, SHOP2PROD
from . import lazada_utils
from . import shopee_utils
from . import tiki_utils


error_logger = logging.getLogger("error_logger")


def create_api(site: str, q: str, s: int) -> str:
    if site == "lazada":
        return API_LIST[site][0].format(s, q)
    if site in ["shopee", "tiki"]:
        return API_LIST[site][0].format(q, s)
    return ""

def create_api_hottrend(site: str, id: int, s: int) -> str:
    if site == 'shopee':
        return HOT_TREND[site][1].format(id,s)
    if site == 'tiki':
        return HOT_TREND[site][1].format(s, id, id)
    return ""

def create_api_shop(site:str, id: int, s:int) ->str:
    if site == 'shopee':
        return SHOP2PROD[site][0].format(s, id)
    return ""

def get_total(site: str, res: dict) -> int:
    if site == "shopee":
        return res["total_count"]

    if site == "tiki":
        return res["paging"]["last_page"]

    return 99999


def get_shopid(site: str, res: dict) -> list:
    if site == "lazada":
        return lazada_utils.get_shopid(res)
    if site == "shopee":
        return shopee_utils.get_shopid(res)
    if site == "tiki":
        return tiki_utils.get_shopid(res)
    return []


def get_shop_url(site: str, logger, keyword: str, lst_id: list):
    try:
        if site == "lazada":
            return lazada_utils.get_shop_url(logger, keyword, lst_id)
        if site == "shopee":
            return shopee_utils.get_shop_url(logger, keyword, lst_id)
        if site == "tiki":
            return tiki_utils.get_shop_url(logger, keyword, lst_id)
    except Exception as e:
        # error_logger.error(f"get_shop_url {e}.")
        print(e)
    finally:
        return []
