#!/usr/bin/env python3
"""Post a thank-you tweet to Elon Musk for the X Money signup bonus."""

import os
import sys
import json
import requests
from requests_oauthlib import OAuth1

TWEET_TEXT = "thanks for the fifteen bucks, Papa Elon @elonmusk"
URL = "https://api.x.com/2/tweets"


def main():
    api_key = os.environ.get("X_API_KEY")
    api_secret = os.environ.get("X_API_SECRET")
    access_token = os.environ.get("X_ACCESS_TOKEN")
    access_secret = os.environ.get("X_ACCESS_SECRET")

    missing = [name for name, val in {
        "X_API_KEY": api_key,
        "X_API_SECRET": api_secret,
        "X_ACCESS_TOKEN": access_token,
        "X_ACCESS_SECRET": access_secret,
    }.items() if not val]
    if missing:
        print(f"Missing env vars: {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)

    auth = OAuth1(api_key, api_secret, access_token, access_secret)
    resp = requests.post(URL, auth=auth, json={"text": TWEET_TEXT})

    if resp.status_code == 201:
        data = resp.json()["data"]
        print(f"Posted! ID: {data['id']}")
        print(f"Text: {data['text']}")
    else:
        print(f"Failed: {resp.status_code}", file=sys.stderr)
        print(json.dumps(resp.json(), indent=2), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
