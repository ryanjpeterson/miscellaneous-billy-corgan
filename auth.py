import tweepy
from api_keys import consumer_key, consumer_secret, access_token, access_token_secret

# Set up API variable, pass api keys into it to authenticate tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)
user = api.me()
