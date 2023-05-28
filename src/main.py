from src.utils import endpoints
from src.utils import secrets
from src.api_requests import *

auth = [f'Bearer={secrets.MY_TWITTER_BEARER}',
        f'API Key={secrets.api_key}',
        f'API Key Secret={secrets.api_key_secret}',
        f'Access Token={secrets.access_token}',
        f'Access Token Secret={secrets.access_token_secret}']

# get_first_twitter_api(endpoints.FIRST_GET_TEST_TWITTER_API, auth)

get_public_tweets(auth)