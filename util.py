import tweepy
import time

# Limit the amount of requests made to API, sleep for 1s if RateLimitError is thrown by Tweepy


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
    except StopIteration:
        return
