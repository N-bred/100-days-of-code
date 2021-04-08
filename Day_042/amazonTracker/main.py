import requests
from bs4 import BeautifulSoup
from time import sleep

URI = "https://www.amazon.com/Razer-Kraken-Ultralight-Gaming-Headset/dp/B07RMC5BRL/ref=sr_1_3?dchild=1&keywords=gaming+headset&qid=1617917049&sr=8-3"
HEADERS = {
    "Host": "www.amazon.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.amazon.com/s?k=gaming+headset&ref=nb_sb_noss_1",
    "Connection": "keep-alive",
    "Cookie": "session-id=139-7238573-2456456; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn='L5Z9:CO'; csm-hit=tb:42SD77PRA2S883N0H391+s-3PKTX38GQRKAG3QHKE71|1617917591469&t:1617917591469&adb:adblk_yes; ubid-main=133-2560363-0225962; session-token=+f63Th3N4Kd5cqalx2uhm/Vxcl0O+nHsXrXTPEFPrkfppfDf8Ia06hOoJdA3K8FRbQDcGG/rZBeQeJv/gwR7LjeIVVApq6dR7tVZTB21A1DnNJcy5T0Ec5CepurHRGk8BrDyw2FAgdiA5FR8zItSkI2SBxQsfW9hBqyQBHFmrygAhpuOiX8QIEtIZIN6ltIB; lc-main=en_US; skin=noskin",
    "Upgrade-Insecure-Requests": "1",
    "Cache-Control": "max-age=0"
}

TRESHOLD = 41


def make_request(url, **kwargs):
    req = requests.get(url, **kwargs)
    req.raise_for_status()
    res = req.text
    return res


def get_prices(markup):
    beautifulSoup = BeautifulSoup(markup, features="lxml")
    price = beautifulSoup.find(
        "span", class_="a-size-medium a-color-price priceBlockBuyingPriceString")
    shipping_container = beautifulSoup.find(
        "span", id="ourprice_shippingmessage")
    shipping_price = shipping_container.find(
        "span", class_="a-size-base a-color-secondary")
    return {"price": float(price.getText()[1:]), "shipping_price": shipping_price.getText()}


def main():
    req = make_request(URI, headers=HEADERS)
    prices = get_prices(req)
    if (prices["price"] <= TRESHOLD):
        print("Buy Now!")


if __name__ == '__main__':
    while True:
        main()
        sleep(2)
