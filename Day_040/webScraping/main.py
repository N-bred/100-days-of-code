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


def main():
    html_code = make_request('https://news.ycombinator.com/')
    soup = BeautifulSoup(html_code, features="lxml")
    scores = soup.find_all(class_="score")
    scores_info = [get_info(score) for score in scores]
    sorted_scores = sorted(scores_info, key=lambda info: info["score"])
    highest_score = sorted_scores[-1]
    article = soup.find(id=highest_score["id"])
    print(parse_article(article))


if __name__ == "__main__":

    main()
