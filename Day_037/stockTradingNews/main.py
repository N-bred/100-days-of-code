from dotenv import load_dotenv
import os
import requests
from datetime import datetime, timedelta
load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
A_MONTH_AGO = (datetime.utcnow().replace(day=1) -
               timedelta(days=1)).strftime("%Y-%m-%d")

STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

NEWS_PARAMS = {
    "q": COMPANY_NAME,
    "from": A_MONTH_AGO,
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY
}


def make_request(url, params):
    req = requests.get(url, params)
    req.raise_for_status()
    return req.json()


def make_article(article):
    return f"\nTitle: {article['title']}\nDescription: {article['description']}\nURL: {article['url']}\n"


def make_message(percentage,  direction="up", articles=[]):
    article_data = []
    symbol = "UP 🔺"
    if direction == "down":
        symbol = "DOWN 🔻"
    if len(articles) != 0:
        article_data = [make_article(article) for article in articles]
    return f"{STOCK}: {symbol} {percentage}%" + '\n\n' + '\n\n'.join(article_data)


def format_data(data):
    data[1]["date"] = data[0]
    return data[1]


def eval_data(json_data):
    stock_data = [format_data(data)
                  for data in json_data["Time Series (Daily)"].items()][:2]
    close1, close2 = float(stock_data[0]["4. close"]), float(
        stock_data[1]["4. close"])
    percentage = (close1 - close2) / close1

    if percentage >= 0.05:
        return (percentage, 'up')
    elif percentage <= -0.05:
        return (percentage, 'down')
    return False


def main():
    data = make_request(STOCK_API_ENDPOINT, STOCK_PARAMS)
    value = eval_data(data)
    if type(value) is not bool:
        news = make_request(NEWS_API_ENDPOINT, NEWS_PARAMS)
        articles = news["articles"][:3]
        message = make_message(value[0], value[1], articles)
        return print(message)
    return print("No substantial changes")


if __name__ == "__main__":
    main()
