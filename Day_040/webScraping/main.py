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


def parse_article(element):
    el = element.find(class_="storylink")
    return f"""
    Title: {el.text}

    URL: {el["href"]}
    """
