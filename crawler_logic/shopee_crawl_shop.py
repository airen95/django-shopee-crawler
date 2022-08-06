# from utils.utils import load_json
from utils.config import SHOP2PROD
from utils.crawler_utils import create_api_shop
from utils.api_utils import send_request
from utils.shopee_utils import get_info_product, get_total

site = 'shopee'
shop_id = 63387678
folder_id = '16kyM02UH6Krf9AlPqmnEHvZLAyp3AYLH'
SPREADSHEET_SHOP_ID = '1QBOfWJcwMe7dOp2kLcjmEEhX8heXRF8mCNoH2_C5TZA'

def crawler(site, prod):

    #get_general:
    info = get_info_product(site, prod)
    # api = SHOP2PROD[site][1].format(info['no'], shop_id)
    # logger.info('Getting detail for item {itemid} from shop {shop_id}')

    # #get_detail:
    # res_detail = send_request(site, api)
    # sub_info = get_product_detail(site, res_detail)
    # info.update(sub_info)
    info['des'], info['cate'] = '', ''
    #Values:
    values = [info['no'], info['title'], info['des'], info['cate'], info['price'], info['price_before_discount'], info['variations'], info['images']]

    return values

if __name__ == '__main__':
    # initialize a google sheet service:
    # auth = load_json("../resource/google-drive.json")
    # service = create_service(auth["creds_file"], auth["api_name"], auth["api_version"], auth["scopes"])

    api = create_api_shop(site, shop_id, 0)
    print(api)
    try:
        res = send_request(site, api)
        total = get_total(site, res)

        print(res)
        # first info:
        for prod in res['data']['sections']['data']['item']:
            values = crawler(site, prod)
        if total > 100:
            for i in range(100, total+1, 100):
                api = create_api_shop(site, shop_id, i)
                print(api)
                res = send_request(site, api)
                for prod in res['data']['sections']['data']['item']:
                    values = crawler(site, prod)
        else:
            print('No more items')

        # # df.to_csv('./shop.csv')
        # filename = f'{shop_id}.csv'
        # # upload_csv_to_sheet(service, filename, folder_id, './shop.csv')
        # # print(df.head())
            # print(values)
    except Exception as err:
        print(err)
