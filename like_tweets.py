import tweepy
import time
from api_keys import consumer_key, consumer_secret, access_token, access_token_secret
from util import limit_handler

# Set up API variable, pass api keys into it to authenticate tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)
user = api.me()


# Pass in array of strings to search, limit of tweets to search
def like_tweets(search_strings_arr, search_limit):
    for search_term in search_strings_arr:
        for tweet in limit_handler(tweepy.Cursor(api.search, search_term).items(int(search_limit))):
            try:
                tweet.favorite()
                print(
                    f'COWBOY CORGAN LIKED: {tweet.text} by {tweet.user.screen_name}')
                print('----------------------------------')
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break


def unlike_my_likes(num):
    i = 0
    for like in limit_handler(tweepy.Cursor(api.favorites).items(int(num))):
        api.destroy_favorite(like.id)
        print(f'Unliked {like.id}')
        i += 1

    print(f'Finished unliking {i} tweets')


def print_my_likes():
    i = 1
    for like in limit_handler(tweepy.Cursor(api.favorites).items()):
        print(f'{i}: {like.id}')
        i += 1


like_tweets(['smashing pumpkins', '90s guitar', 'billy corgan'], 25)
# unlike_my_likes(175)
# print_my_likes()
