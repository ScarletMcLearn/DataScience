import sys
import json
from tweepy import Cursor
from twitter_client import get_twitter_client
import time

client = get_twitter_client()

user_list = ['jenadvisesyou', 'georgianbayjen', 'jesswaatt', 'rachelcantu', 'nicolenicklass', 'jordanrrye', 'TenaciousTess', 'kne_14']

for user in user_list:
    print('Started...')
    fname = "user_timeline_{}.jsonl".format(user)
    with open(fname, 'w') as f:
        for page in Cursor(client.user_timeline, screen_name=user, count=200).pages(16):
            for status in page:
                f.write(json.dumps(status._json)+"\n")

    print('Completed!')
    
    print('Sleeping...')
    time.sleep(20*60)