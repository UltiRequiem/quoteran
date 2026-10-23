"""
Fetch a random quote from a Quotable server and print it.

The server is configurable: the --api-url flag, then the QUOTABLE_API_URL
environment variable, then the public default.
"""
import argparse
import os
import sys
from typing import List, Optional

import requests

from .ui import cprint, cyan

DEFAULT_API_URL = "https://api.quotable.io"
API_URL_ENV = "QUOTABLE_API_URL"

# Kept for backwards compatibility: the full URL of the default random endpoint.
API = DEFAULT_API_URL + "/random"


def get_base_url(explicit: Optional[str] = None) -> str:
    """
    The server to talk to: the explicit value, then $QUOTABLE_API_URL, then the
    public default. Trailing slashes are removed.
    """
    return (explicit or os.environ.get(API_URL_ENV) or DEFAULT_API_URL).rstrip("/")


def random_quote_url(base_url: Optional[str] = None) -> str:
    """The URL of the random quote endpoint on the configured server."""
    return get_base_url(base_url) + "/random"


def fetch_and_parse(api: str) -> dict:
    """Get a URL and parse the JSON answer, raising for non 2xx statuses."""
    response = requests.get(api, timeout=10)
    response.raise_for_status()
    return response.json()


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    """Read the command line."""
    parser = argparse.ArgumentParser(prog="quoteran", description="Random quotes on terminal.")
    parser.add_argument(
        "--api-url",
        help=f"base URL of a Quotable server (default: ${API_URL_ENV}, then {DEFAULT_API_URL})",
    )
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> None:
    """Print a random quote."""
    args = parse_args(argv)

    try:
        data = fetch_and_parse(random_quote_url(args.api_url))
    except (requests.RequestException, ValueError) as error:
        print(f"Could not get a quote from {get_base_url(args.api_url)}.", file=sys.stderr)
        print(
            f"Pass --api-url or set {API_URL_ENV} to point at a running Quotable server.",
            file=sys.stderr,
        )
        print(error, file=sys.stderr)
        sys.exit(1)

    cprint(data["content"], cyan)
    cprint(f" - {data['author']}")
