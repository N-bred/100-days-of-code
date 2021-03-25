from bs4 import BeautifulSoup
import requests


def make_request(url, params={}):
    req = requests.get(url)
    req.raise_for_status()
    return req.content


def get_info(element):
    return {
        "id": element["id"].split("_")[1],
        "score": int(element.text.split(" ")[0])
    }