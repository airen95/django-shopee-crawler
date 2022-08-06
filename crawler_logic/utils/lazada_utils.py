import logging
from unidecode import unidecode

from .config import API_LIST
from .text_utils import percent_decode


error_logger = logging.getLogger("error_logger")


def get_shopid(res: dict) -> list:
    lst_id = []
    for i in res["mods"]["listItems"]:
        id_ = i["sellerName"]
        lst_id.append(id_)

    return lst_id


def get_shop_url(logger, keyword: str, lst_id: list) -> list[list[str]]:
    values = []
    for id_ in lst_id:
        try:
            # logger.info(f"Getting info of {id_} ...")
            shop = unidecode(id_).split()
            shop = "-".join(shop)
            path = API_LIST["lazada"][1].format(shop)
            values.append([percent_decode(keyword), path])
        except Exception as e:
            # error_logger.error(f"Lazada cralwer error {e} for {id_}")
            print(e)

    return values
