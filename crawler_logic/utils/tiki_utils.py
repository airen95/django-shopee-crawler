import logging

from .config import API_LIST, CATE
from .api_utils import send_request
from .text_utils import percent_decode
from typing import List, Dict


error_logger = logging.getLogger("error_logger")


def get_shopid(res: dict) -> list:
    lst_id = []
    for i in res["data"]:
        id_ = i["seller_id"]
        lst_id.append(id_)

    return lst_id


def get_shop_url(logger, keyword: str, lst_id: list) -> List[List[str]]:
    values = []
    for id_ in lst_id:
        url = API_LIST["tiki"][1].format(id_)
        try:
            # logger.info(f"Request info for {id_} ...")
            res = send_request("tiki", url)
            if len(res) == 0:
                continue
            path = res["data"]["seller"]["url"]
            values.append([percent_decode(keyword), path])
        except Exception as e:
            # error_logger.error(f"Tiki cralwer error {e} for {id_}")
            print(e)

    return values

def get_product_name(site: str, id: int, res: dict) -> List[List[str]]:
    values = []
    for i in res['data']:
        name = i['name']
        val = [CATE[site][id], name]
        values.append(val)
    return values

