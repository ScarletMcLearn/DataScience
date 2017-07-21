import tweepy

consumer_key = 'F8rPAdtXOLkmrKQySWE0APDaa'
consumer_secret = 'TtD0czxBRcydqEDtC80X2lqM7lPUigVumUuBZS3K94a27uriuG'
access_token = '149863732-xSwmL051gcdlpAVeFMN3nvjoLEkFGup1DPPPd6VK'
access_token_secret = 'B55TjcosWOSLodPSyWhK37MGTk0u3xFWISI7MvaW5SDyG'

print("Welcome to the Twiscrapper API")
print("This will let you Stream Public Tweets From Twitter Based On KeyWords")
print("And a lot more. ;) ")
print()

print()
print("First make a Twitter Developer Account and Setup a new app and get its keys.")
print()
print("Paste the keys with NO spaces! ")
print()

# consumer_key = input("Please paste your Consumer Key: (F8XXXXXXXXXXXXXXXXXX)")
# consumer_secret = input("Please paste your Consumer Secret: (TtD0XXXXXXXXXXXXXXXXXXXXXXXXXXXXX)")
# access_token = input("Please paste your Access Token: (XXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXX)")
# access_token_secret = input("Please paste your Access Token Secret: (XXXXXXXXXXXXXXXXXXXXXXXXXXXX)")
key_word = input("Please enter the Key Word by which you want to Stream Live Tweets: (books / Donald Trump) ")
infinite_stream_checker = input("Please enter if you want to stream infinite live Tweets on " + key_word + " or an amount of Tweets: 0 - Infinite Tweets ON, 1 - Infinite Tweets OFF ")

counter = ""

if (infinite_stream_checker != "0"):
    counter = int(input("Please enter how many Tweets you want to Stream: "))


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


if (infinite_stream_checker == '0'):
        while True:
            try:
                twitterStream = tweepy.Stream(auth, listener())
                twitterStream.filter(track=[key_word])
            except:
                continue

else:
    value = 0
    while(counter > 0):
        # while True:
            try:
                ++value

                twitterStream = tweepy.Stream(auth, listener())

                print(str(value) + "th Tweet with keyword " + key_word +": ")
                twitterStream.filter(track=[key_word])
                print()
                --counter
            except:
                continue
