import requests

from .ui import cprint, cyan

API = "https://api.quotable.io/random"


def fetch_and_parse(api: str) -> dict:
    return requests.get(api).json()


def main() -> None:
    data = fetch_and_parse(API)
    cprint(data["content"], cyan)
    cprint(f" - {data['author']}")
