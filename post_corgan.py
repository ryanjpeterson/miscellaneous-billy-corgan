import random
import os
import tweepy
import time
import shutil
import pathlib
from api_keys import consumer_key, consumer_secret, access_token, access_token_secret


# Set up API variable, pass api keys into it to authenticate tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

# Get random image from /img folder inside project directory


def get_random_corgan():
    return random.choice(os.listdir('./img/queue'))

# Upload image to Twitter account


def upload_random_corgan(file, caption):
    return api.update_with_media(f'./img/queue/{file}', status=caption)

# Move image to /posted folder inside project directory


def move_corgan_to_posted_folder(file):
    current_dir = pathlib.Path(__file__).parent.absolute()
    src_path = f'{current_dir}/img/queue/{file}'
    dest_path = f'{current_dir}/img/posted'
    shutil.move(src_path, dest_path, copy_function='copy2')

# Main function to execute Corganposting


def main():
    file = get_random_corgan()
    caption = file.split('.')[0]

    try:
        media = upload_random_corgan(file, caption)
    except:
        print('Something went wrong...')

    move_corgan_to_posted_folder(file)

    print(media)
    print(f'Successfully posted a Corgan')


# Execute main function if file __name__ == __main__
if __name__ == '__main__':
    main()
