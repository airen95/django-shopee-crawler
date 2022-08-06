import random


SPREADSHEET_SHOP_ID = '1NZ3Q0p9ywd_EFuJLN3-QWkTVB_uRXZCDxtbcbToWgU0'


"""
lst[0] : initialize firts page/newest to get total products
lst[1]: to start the loop after getting total
lst[2]: offset step 100, page step 1 per loop
"""
SUPPLEMENT = {
    "lazada": [0, 1, 1],
    "shopee": [0, 100, 100],
    "tiki": [1, 2, 1]
}


"""
lst[0] : search api
lst[1]: shop info api
"""
API_LIST = {
    "lazada": ["https://www.lazada.vn/catalog/?_keyori=ss&ajax=true&page={}&q={}",
               "https://www.lazada.vn/shop/{}"],
    "shopee": ["https://shopee.vn/api/v4/search/search_items?by=relevancy&keyword={}&limit=100&newest={}",
               "https://shopee.vn/api/v4/product/get_shop_info?shopid={}"],
    "tiki": ["https://tiki.vn/api/v2/products?limit=100&q={}&page={}",
             "https://tiki.vn/api/shopping/v2/widgets/seller?seller_id={}"]
}

HOT_TREND = {
    "shopee": ['https://shopee.vn/api/v4/pages/get_homepage_category_list',\
                # 'https://shopee.vn/api/v4/search/search_items?by=sales&limit=100&match_id={}&newest={}' ],\
                'https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=100&match_id={}&newest={}'],
    "lazada": ['https://pages.lazada.vn/wow/i/vn/LandingPage/lp-collection-detail-new?spm=a2o4n.collection.content.1.73314c07djstjp&wh_weex=true&wx_navbar_transparent=true&abtest=&pos=1&abbucket=&clickTrackInfo=1007.16900.95383.100200300000000_fc17c495-308c-419d-8377-942690ff75c1_0__vn_2174106_0%3A0_1127376279_9_0.2423918661428059__1_360738408_9_0.16440915199893186__2_1031782524_9_0.1188896040213498__3_121017539_9_0.0__4_351640246_9_0.0__5_855002016_9_0.0__6_1089312480_9_0.0&themeID=2174106&acm=201711100.1003.1.2262599&algArgs=2174106_1127376279-360738408-1031782524-121017539-351640246-855002016-1089312480&scm=1007.16900.95383.100200300000000',\
                'https://pages.lazada.vn/wow/i/vn/LandingPage/lp-collection-detail-new?spm=a2o4n.collection.content.5.21574c07vMqVPe&wh_weex=true&wx_navbar_transparent=true&abtest=&pos=5&abbucket=&clickTrackInfo=1007.16900.95383.100200300000000_c671d784-92e4-415a-b5e6-77292f11396c_0__vn_2174105_4%3A0_1277935695_9_0.6540076806578029__1_1029176229_9_0.28173829639447145__2_1043528127_9_0.18651582553682722__3_868686900_9_0.0__4_807310499_9_0.0__5_910298101_9_0.0__6_102330096_9_0.0&themeID=2174105&acm=201711100.1003.1.2262599&algArgs=2174105_1277935695-1029176229-1043528127-868686900-807310499-910298101-102330096&scm=1007.16900.95383.100200300000000'],\
    
    'tiki': ['https://api.tiki.vn/v2/categories?parent_id=2',\
            'https://tiki.vn/api/personalish/v1/blocks/listings?limit=100&page={}&sort=top_seller&categoryId={}&category={}']

}

CATE = {'shopee': {11035567: 'Men Clothes', 11035639: 'Women Clothes', 11036030: 'Mobile & Gadgets',\
        11036194: 'Moms, Kids & Babies', 11036132: 'Consumer Electronics', 11036670: 'Home & Living', \
        11035954: 'Computer & Accessories', 11036279: 'Beauty & Personal Care', 11036101: 'Cameras', \
        11036345: 'Health', 11035788: 'Watches', 11035825: 'Women Shoes', 11035801: 'Men Shoes', \
        11035761: 'Women Bags', 11036971: 'Home Appliances', 11035853: 'Fashion Accessories', \
        11035478: 'Sport & Outdoor', 11036525: 'Grocery', 11036793: 'Automotive', 11036863: 'Books & Stationery', \
        11035741: 'Men Bags', 11036382: 'Kid Fashion', 11036932: 'Toys', 11036624: 'Home care', 11036478: 'Pets', \
        11082137: 'Deals Near Me', 11035898: 'Tickets, Vouchers & Services'},\
        'tiki': {2549: 'Đồ Chơi - Mẹ & Bé', 44792: 'NGON', 1789: 'Điện Thoại - Máy Tính Bảng', 1520: 'Làm Đẹp - Sức Khỏe', 1882: 'Điện Gia Dụng', 931: 'Thời trang nữ', 915: 'Thời trang nam', 1703: 'Giày - Dép nữ', 976: 'Túi thời trang nữ', 1686: 'Giày - Dép nam', 27616: 'Túi thời trang nam', 6000: 'Balo và Vali', 27498: 'Phụ kiện thời trang', 8371: 'Đồng hồ và Trang sức', 1846: 'Laptop - Máy Vi Tính - Linh kiện', 1883: 'Nhà Cửa - Đời Sống', 17166: 'Hàng Quốc Tế', 4384: 'Bách Hóa Online', 1815: 'Thiết Bị Số - Phụ Kiện Số', 11312: 'Voucher - Dịch vụ', 8594: 'Ô Tô - Xe Máy - Xe Đạp', 8322: 'Nhà Sách Tiki', 4221: 'Điện Tử - Điện Lạnh', 1975: 'Thể Thao - Dã Ngoại', 1801: 'Máy Ảnh - Máy Quay Phim'}
}

SHOP2PROD = {'shopee': ['https://shopee.vn/api/v4/shop/get_products_tab_data?by=popular&limit=100&offset={}&order=desc&shop_id={}',\
                        'https://shopee.vn/api/v4/item/get?itemid={}&shopid={}']
    }