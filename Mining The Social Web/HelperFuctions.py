# import json

# alltweets = []  


# def get_all_tweets(name, screen_name):
#     #Twitter only allows access to a users most recent 3240 tweets with this method

#     #authorize twitter, initialize tweepy
# #     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# #     auth.set_access_token(access_key, access_secret)
# #     api = tweepy.API(auth)

#     #initialize a list to hold all the tweepy Tweets
#     alltweets[name] = [] 

#     #make initial request for most recent tweets (200 is the maximum allowed count)
#     new_tweets = api.GetUserTimeline(screen_name = screen_name,count=200)

#     #save most recent tweets
#     alltweets.extend(new_tweets)

#     #save the id of the oldest tweet less one
#     oldest = alltweets[-1].id - 1

#     #keep grabbing tweets until there are no tweets left to grab
#     while len(new_tweets) > 0:
#         print ("getting tweets before %s" % (oldest))

#         #all subsiquent requests use the max_id param to prevent duplicates
#         new_tweets = api.GetUserTimeline(screen_name = screen_name,count=200,max_id=oldest)

#         #save most recent tweets
#         alltweets.extend(new_tweets)

#         #update the id of the oldest tweet less one
#         oldest = alltweets[-1].id - 1
    
#         print ("...%s tweets downloaded so far" % (len(alltweets)))

#     #transform the tweepy tweets into a 2D array that will populate the csv	
#     outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

#     #write the csv	
# #     with open('%s_tweets.csv' % screen_name, 'wb') as f:
# #         writer = csv.writer(f)
# #         writer.writerow(["id","created_at","text"])
# #         writer.writerows(outtweets)

#     pass






# NEW TRY


def get_all_tweets(name, screen_name):
    alltweets = [] 

    new_tweets = api.GetUserTimeline(screen_name = screen_name,count=200)

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print ("getting tweets before %s" % (oldest))

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.GetUserTimeline(screen_name = screen_name,count=200,max_id=oldest)

        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
    
        print ("...%s tweets downloaded so far" % (len(alltweets)))

        return alltweets
  


import json

def jsonify(name, tweets):
    data = {} 
    data[name] = []  


    for stat in tweets:
        data[name].append(stat.AsJsonString())
    
    return data
