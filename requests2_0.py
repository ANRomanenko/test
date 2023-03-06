import requests
from apikey import API_TOKEN_2


def download(q: str):
    header = {"Authorization": API_TOKEN_2}
    url = f"https://api.pexels.com/v1/search?query={q}&per_page=1"
    r = requests.get(url, header=header)
    print(r)


def main() -> None:
    q = input("Query: ")
    download(q)

main()