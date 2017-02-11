import tweepy
from textblob import TextBlob


consumer_key = 'Rr8bvMl6meufSR27xZJyQYMzo'
secret_key = 'SfwcCZNRpZxXbMtHqVJGQ1zTSkrtNQRt6K30ESAETTi1PQRhyZ'

access_token = '149863732-WxX618Vyq5h5yQygCC1v3w2jBYrd8tGbmf7chCKX'
access_token_secret = 'z6S763e6ICP2RliCxdiYdiXgGcoZmp7EmHFoaQ2TUQtvP'


auth = tweepy.OAuthHandler(consumer_key, secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print (analysis.sentiment)
