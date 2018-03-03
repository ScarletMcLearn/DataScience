
# coding: utf-8

# In[1]:


import twitter


# In[2]:


api = twitter.Api(consumer_key='4fsyL9GWIQkbXi9hHJcVDpm4L',
                      consumer_secret='ekOHjtbvWCltUTkMX9qC3YwxAZmU9QgnIetKd1hfzMLKP41HIn',
                      access_token_key='149863732-hCncnsL7EDkgaujC5WRZl3oGCYNaaCDttyjcYVxU',
                      access_token_secret='AcELcldQyLIIKz78LLr6JYiscjRBMJKM7b6CLA1gg86rS')


# In[3]:


print(api.VerifyCredentials())


# In[5]:


twitter_api = twitter.Twitter(auth=auth)


# In[4]:


statuses = api.GetUserTimeline(screen_name='scarlet')


# In[5]:


statuses


# In[8]:


users = api.GetFriends()


# In[9]:


users


# In[10]:


api


# In[13]:


WORLD_WOE_ID = 1
US_WOE_ID = 23424977


# In[14]:


DHAKA_WOE_ID = 1915035
BANGLADESH_WOE_ID = 23424759


# In[15]:


twitter_api = api
world_trends = twitter_api.GetTrendsWoeid(woeid=WORLD_WOE_ID)
us_trends = twitter_api.GetTrendsWoeid(woeid=US_WOE_ID)

# bd_trends = twitter_api.GetTrendsWoeid(woeid=BANGLADESH_WOE_ID)
# dk_trends = twitter_api.GetTrendsWoeid(woeid=DHAKA_WOE_ID)


# In[13]:


help(api)


# In[16]:


print(world_trends)


# In[17]:


print(us_trends)


# In[12]:


import pprint


# In[19]:


pprint.pprint(world_trends)


# In[20]:


pprint.pprint(us_trends)


# In[14]:


import json


# In[22]:


print (json.dumps(world_trends, default=lambda o: o.__dict__, indent=1))


# In[23]:


print (json.dumps(us_trends, default=lambda o: o.__dict__, indent=1))


# In[24]:


world_trends_set = set([trend['name']
                     for trend in world_trends[0]['trends']])

us_trends_set = set([trend['name']
                     for trend in us_trends[0]['trends']])

common_trends = world_trends_set.intersection(us_trends_set)

print(common_trends)


# In[25]:


type(json.dumps(us_trends, default=lambda o: o.__dict__))


# In[26]:


a = json.dumps(us_trends, default=lambda o: o.__dict__, indent=1)


# In[27]:


a['name']


# In[28]:


(list(us_trends)[0]).AsDict()['name']


# world_trends_set = set([trend['name']
#  for trend in world_trends[0]['trends']])
# us_trends_set = set([trend['name']
#  for trend in us_trends[0]['trends']])
# common_trends = world_trends_set.intersection(us_trends_set)
# print common_trends

# In[30]:


world_trends_set = set([trend['name']
 for trend in world_trends[0]['trends']])
us_trends_set = set([trend['name']
 for trend in us_trends[0]['trends']])
common_trends = world_trends_set.intersection(us_trends_set)
print (common_trends)


# In[40]:


q = 'depressed'


# In[41]:


count = 100


# In[42]:


search_results = twitter_api.GetSearch(term=q, count=count)
# statuses = search_results['statuses']

search_results


# In[57]:


for item in range(5):
    pprint.pprint(search_results[item])
    print()
    print(type(search_results[item]))
    


# In[59]:


help(twitter.models.Status)


# In[62]:


search_results[0].AsDict()


# In[63]:


tweet_bank = [s.AsDict() for s in search_results]


# In[64]:


tweet_bank


# In[65]:


tweet_bank[0]['text']


# In[66]:


from collections import Counter


# In[5]:


# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
# from twitter import Api, OAuth, TwitterHTTPError, TwitterStream


# In[7]:


twitter_stream = TwitterStream(api)


# In[ ]:


# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 1000
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print json.dumps(tweet)  
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break 


# In[9]:


statuses[0]


# In[8]:


statuses[0].AsJsonString


# In[13]:


pprint.pprint(statuses[0].AsJsonString)


# In[19]:


type(statuses[0].AsJsonString())


# In[20]:


statuses[0].AsJsonString()


# In[22]:


pprint.pprint(statuses[0].AsJsonString(), indent=4)


# In[23]:


type(statuses[0].AsJsonString())


# In[29]:


import json

# data = dict(statuses)  

type(statuses)

# with open('json test 2.txt', 'a') as outfile:  
#     for stat in statuses:
        
#         json.dump(data, outfile)


# In[30]:


import json

data = {}  
data['Me'] = []  
# data['people'].append({  
#     'name': 'Scott',
#     'website': 'stackabuse.com',
#     'from': 'Nebraska'
# })
# data['people'].append({  
#     'name': 'Larry',
#     'website': 'google.com',
#     'from': 'Michigan'
# })
# data['people'].append({  
#     'name': 'Tim',
#     'website': 'apple.com',
#     'from': 'Alabama'
# })

for stat in statuses:
    data['Me'].append(stat.AsJsonString())

with open('json test 2.txt', 'w') as outfile:  
    json.dump(data, outfile)


# In[35]:


alltweets = []  

def get_all_tweets(name, screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
#     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_key, access_secret)
#     api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
#     alltweets[name] = [] 

    #make initial request for most recent tweets (200 is the maximum allowed count)
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

    #transform the tweepy tweets into a 2D array that will populate the csv	
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

    #write the csv	
#     with open('%s_tweets.csv' % screen_name, 'wb') as f:
#         writer = csv.writer(f)
#         writer.writerow(["id","created_at","text"])
#         writer.writerows(outtweets)

    pass



# In[ ]:


get_all_tweets("Me", "essenceprimus")


# In[37]:


alltweets


# In[60]:


import json

# data = {} 

def jsonify(name, tweets):
    data = {} 
    data[name] = []  


    for stat in tweets:
        data[name].append(stat.AsJsonString())
    
    return data
    
j = jsonify("Meh", alltweets)


# In[61]:


j


# In[46]:


len(statuses)


# In[54]:


data["Me"] = []

for stat in alltweets:
        data["Me"].append(stat.AsJsonString())


# In[55]:


data


# In[58]:


j


# In[59]:


type(j)


# In[67]:


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
    
a = get_all_tweets('Ratul', 'essenceprimus')


# In[68]:


a = get_all_tweets('Ratul', 'essenceprimus')


# In[69]:


a

