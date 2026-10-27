# X Money Thanks Bot

Posts a thank-you tweet to Elon Musk for the X Money signup bonus.

## Setup

1. Create a developer account and app at https://developer.x.com
2. Get your API key, API secret, access token, and access token secret (OAuth 1.0a User Context)
3. Install dependencies: `pip install -r requirements.txt`
4. Export your credentials:
   ```bash
   export X_API_KEY=...
   export X_API_SECRET=...
   export X_ACCESS_TOKEN=...
   export X_ACCESS_SECRET=...
   ```
5. Run: `python post_thanks.py`

## Tweet

`thanks for the fifteen bucks, Papa Elon @elonmusk`

Edit `TWEET_TEXT` in `post_thanks.py` to customize.
