import requests
import tweepy

from src.utils import utils


def get_first_twitter_api(endpoint, auth):
    headers = {'Authorization': f'Bearer {utils.parse_secret(auth[0])}'}

    response = requests.get(endpoint, headers=headers)
    result = response.json()

    print(result)
    return result


def get_public_tweets(auth):
    authentic = tweepy.OAuthHandler(utils.parse_secret(auth[1]), utils.parse_secret(auth[2]))
    authentic.set_access_token(utils.parse_secret(auth[3]), utils.parse_secret(auth[4]))

    api = tweepy.API(authentic)

    public_tweets = api.home_timeline()

    print(public_tweets)
    return public_tweets
