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



def jsonify_tweets(name, tweets):
    data = {} 
    data[name] = []  


    for stat in tweets:
        data[name].append(stat.AsJsonString())
    
    return data



# SAVING THE JSON TWEETS





#EXTRACTING IMAGES AND TEXT AS DICT FROM IMAGE CATG RESULT PAGE
def txt_img_extract(res_page):
    txt_img_dic = {}
    try:
        res_pg = requests.get(res_page)


    except requests.ConnectionError:
        print('Connection Error(s) occured. :( : ' + requests.ConnectionError)

    res_page_soup = BeautifulSoup(res_pg.content, 'html5lib')

    img_box = res_page_soup.findAll('div', {'class':'m-brick grid-item boxy bqQt'})

    for itm in img_box:
        try:
            img_t = itm.find('img')['alt']
            img_l = 'https://www.brainyquote.com' + itm.find('img')['src'].replace('.jpg', '-2x.jpg')

            txt_img_dic[img_t] = img_l
        except:
            pass
        
    return txt_img_dic



#CONVERT THE CRAPPED DIC TO LIST
def txt_img_d2l(dict_t_i):
    img_lst = []
    for i in range(len(dict_t_i)):
        img_lst.append([list(f.keys())[i], list(f.values())[i]])
    return img_lst   





#GETTING COMPLETE LIST
def complete_img_l(img_lst):
    for i in range(len(img_lst)):
        frm_2 = img_lst[i][1].replace('1-2x.jpg', '2-2x.jpg')
        frm_3 = img_lst[i][1].replace('1-2x.jpg', '3-2x.jpg')
        frm_4 = img_lst[i][1].replace('1-2x.jpg', '4-2x.jpg')
        frm_5 = img_lst[i][1].replace('1-2x.jpg', '5-2x.jpg')
        
        img_lst[i].append(frm_2)
        img_lst[i].append(frm_3)
        img_lst[i].append(frm_4)
        img_lst[i].append(frm_5)
        
    return img_lst




import pickle

def picklify_lst(lst, fn):
    with open(fn+".txt", "wb") as fp:   #Pickling
        pickle.dump(lst, fp)
    print('Completed Picklifying.\n\n')
        
def pickle_loader(fn):
    with open(fn, "rb") as fp:   # Unpickling
        b = pickle.load(fp)
    print('Completed Loading.\n\n')
    return b
        