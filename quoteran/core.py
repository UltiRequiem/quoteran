import requests

API = "https://api.quotable.io/random"


def fetch_and_parse(api: str) -> dict:
    return requests.get(api).json()


def run() -> None:
    DATA = fetch_and_parse(API)
    print(DATA["content"])
    print(f" - {DATA['author']}")
