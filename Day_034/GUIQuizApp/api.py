import requests


def get_questions(url, **kwargs):
    res = requests.get(url, params=kwargs)
    res.raise_for_status()
    return res.json()["results"]
