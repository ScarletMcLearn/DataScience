import tweepy

consumer_key = 'F8rPAdtXOLkmrKQySWE0APDaa'
consumer_secret = 'TtD0czxBRcydqEDtC80X2lqM7lPUigVumUuBZS3K94a27uriuG'
access_token = '149863732-xSwmL051gcdlpAVeFMN3nvjoLEkFGup1DPPPd6VK'
access_token_secret = 'B55TjcosWOSLodPSyWhK37MGTk0u3xFWISI7MvaW5SDyG'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets = api.home_timeline()

for tweet in public_tweets:
    print (tweet.text)


import json
import tweepy
# t = tweepy.Twitter(domain='api.twitter.com', api_version='1')
# print (json.dumps(t.trends(), indent=1))

from tweepy.streaming import StreamListener

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]

        username = all_data["user"]["screen_name"]

#         c.execute("INSERT INTO taula (time, username, tweet) VALUES (%s,%s,%s)",
#             (time.time(), username, tweet))

#         conn.commit()

        print((username,tweet))

        return True

    def on_error(self, status):
        print (status)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# twitterStream = tweepy.Stream(auth, listener())
# twitterStream.filter(track=["book"])



# def start_stream():
#     while True:
#         try:
#             sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))
#             sapi.filter(track=['book'])
#         except:
#             continue
#
# start_stream()


while True:
    try:
        twitterStream = tweepy.Stream(auth, listener())
        twitterStream.filter(track=["book"])
    except:
        continue
