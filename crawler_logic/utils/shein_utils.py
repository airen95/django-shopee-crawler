# from config import SHEIN


def get_breadcumb(res):
  bc = []
  bc.append(res['info']['goods']['parentCats']['cat_url_name'])
  bc+= [i['cat_url_name'] for i in res['info']['goods']['parentCats']['children']]
  return bc

def get_goods_id(res):
  lst = [i['goods_id'] for i in res['goods']]
  return lst

def get_images(res):
  thumbnail = 'https:'+ res['info']['goods']['goods_imgs']['main_image']['origin_image']
  imgs = ['https:' + i['origin_image'] for i in res['info']['goods']['goods_imgs']['detail_image']]
  return [thumbnail, imgs]

def get_relations(res):
  ids = [i['goods_id'] for i in res['info']['goods']['relationProducts']]
  return ids

def get_price(res):
  return res['info']['goods']['detail']['salePrice']['amount']


def get_attr(res):
  attr = {}
  for i in res['info']['goods']['detail']['productDetails']:
    attr[i['attr_name_en']] = i['attr_value_en']
  return attr