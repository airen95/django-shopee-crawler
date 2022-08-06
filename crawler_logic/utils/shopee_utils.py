import logging

from .config import API_LIST, CATE
from .api_utils import send_request
from .text_utils import percent_decode
from typing import List, Dict, Tuple


error_logger = logging.getLogger("error_logger")


def get_shopid(res: dict) -> list:
    lst_id = []
    for i in res["items"]:
        id_ = i["shopid"]
        lst_id.append(id_)

    return lst_id


def get_shop_url(logger, keyword: str, lst_id: list) -> List[List[str]]:
    values = []
    for id_ in lst_id:
        url = API_LIST["shopee"][1].format(id_)
        try:
            # logger.info(f"Request info for {id_} ...")
            res = send_request("shopee", url)
            if len(res) == 0:
                continue
            path = "https://shopee.vn/" + res["data"]["account"]["username"]
            values.append([percent_decode(keyword), path])
        except Exception as e:
            # error_logger.error(f"Shopee cralwer error {e} for {id_}")
            print(e)

    return values

def get_product_name(site: str, id: int, res: dict) -> List[List[str]]:
    values = []
    if site == 'shopee':
        for i in res["items"]:
            name = i["item_basic"]["name"]
            values.append([CATE[site][id], name])
    return values


# for shopee_crawl_shop.py
def get_info_product(site: str, prod: dict):
    info = {}
    if site == 'shopee':
        info['no'] = prod['itemid']
        info['title'] = prod['name']
        info['images'] = prod['images']

        #video_url:
        if prod['video_info_list'] is not None:
            info['vid_url'] = prod['video_info_list'][0]['video_id']
        else:
            info['vid_url'] = ''

        # print('variation')
        #variations:
        info['variations'] = {}
        for var in prod['tier_variations']:
            if len(var['name']) >0:
                info['variations'].update({var['name'] : var['options']})

        info['price']= prod['price']
        # info['price_min'] = prod['price_min']
        # info['price_max ']= prod['price_max']
        info['price_before_discount'] = prod['price_before_discount']
        return info
    return ''

def get_product_detail(site: str, res: dict) -> Dict:
    detail = res['data']
    sub_info = {}
    sub_info['des'] = detail['description']
    sub_info['cate'] = [i['display_name'] for i in detail['categories']]
    return sub_info

def get_total(site: str, res: dict) -> int:
    total = res['data']['sections']['total']
    return total



    

