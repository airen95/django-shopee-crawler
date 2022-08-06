from unidecode import unidecode
import urllib.parse


def manual_encode(keyword: str, site: str) -> str:
    keyword = unidecode(keyword).split()  # type: ignore
    if site in ["shopee", "lazada"]:
        keyword = "%20".join(keyword)
    else:
        keyword = "+".join(keyword)
    return keyword


def percent_encode(keyword: str) -> str:
    keyword = urllib.parse.quote(keyword.encode("utf8"))
    return keyword


def percent_decode(keyword: str) -> str:
    keyword = urllib.parse.unquote(keyword)
    return keyword

# print(percent_encode("kem chống nắng"))
