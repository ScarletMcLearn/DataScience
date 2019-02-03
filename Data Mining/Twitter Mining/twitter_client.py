# Chap02-03/twitter_client.py
import os
import sys
from tweepy import API
from tweepy import OAuthHandler

# def get_twitter_auth():
#     """Setup Twitter authentication.
#     Return: tweepy.OAuthHandler object
#     """
#     try:
#         consumer_key = '4fsyL9GWIQkbXi9hHJcVDpm4L'
#         consumer_secret = 'ekOHjtbvWCltUTkMX9qC3YwxAZmU9QgnIetKd1hfzMLKP41HIn'
#         access_token = '149863732-hCncnsL7EDkgaujC5WRZl3oGCYNaaCDttyjcYVxU '
#         access_secret = 'AcELcldQyLIIKz78LLr6JYiscjRBMJKM7b6CLA1gg86rS'
#     except KeyError:
    #     sys.stderr.write("TWITTER_* environment variables not set\n")
    #     sys.exit(1)    
    # auth = OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_secret)
    # return auth


# consumer_key = '4fsyL9GWIQkbXi9hHJcVDpm4L'
# consumer_secret = 'ekOHjtbvWCltUTkMX9qC3YwxAZmU9QgnIetKd1hfzMLKP41HIn'
# access_token = '149863732-hCncnsL7EDkgaujC5WRZl3oGCYNaaCDttyjcYVxU '
# access_secret = 'AcELcldQyLIIKz78LLr6JYiscjRBMJKM7b6CLA1gg86rS'

# auth = OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_secret)

# def get_twitter_client(auth):
#     """Setup Twitter API client.
#     Return: tweepy.API object
#     """
#     # auth = get_twitter_auth()
#     client = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#     return client

# Chap02-03/twitter_client.py
import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    """Setup Twitter authentication.
    Return: tweepy.OAuthHandler object
    """
    try:
        consumer_key = os.environ['TWITTER_CONSUMER_KEY']
        consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
        access_token = os.environ['TWITTER_ACCESS_TOKEN']
        access_secret = os.environ['TWITTER_ACCESS_SECRET']
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    """Setup Twitter API client.
    Return: tweepy.API object
    """
    auth = get_twitter_auth()
    client = API(auth)
    return client


# 10 PM - 20 mins