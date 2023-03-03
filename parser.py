import requests
from bs4 import BeautifulSoup
import csv

CSV = "cards.csv"
HOST = "https://comfy.ua/"
URL = "https://comfy.ua/smartfon/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
}


def get_html(url, params=""):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(url):
    soup = BeautifulSoup(url, "lxml")
    items = soup.find_all("div", class_="products-list-item")
    return items


html = get_html(URL)
print(get_content(html.text))
