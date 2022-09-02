# This program scrapes the data from twitter

import tweepy
from dotenv import load_dotenv
import os
from pprint import pprint
import json
from datetime import datetime
import time

load_dotenv()

consumer_key = os.getenv("API_Key")
consumer_secret = os.getenv("API_Secret_key")
access_token = os.getenv("Access_Token")
access_token_secret = os.getenv("Access_Token_Secret")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


search_word = "china -filter:retweets -filter:replies"

# for getting the since id:
# temp_search = api.search_tweets(q=search_word, tweet_mode='extended', count=10)
# tlist = [tweet.created_at for tweet in temp_search]
# since_id = tlist[-1]
# for i in tlist:
#     print(i)

"""
Alright, the thing that is wrong is: we get the latest tweet first and hence if we try to get one tweet
and set it as since_id below, it will not return anything, since since_id give all the tweet after that id
but we are using the latest tweet itself, what we could do is, get the 100 tweet and use the oldest id as
since id and then below, if using while loop for 15 minutes, update that since id using the latest id, 
why latest below? because we already fetched the latest below and it doesn't make sense to fetech it again
therefore use latest_id in while loop and set it as since id. 
"""

# TO DO:
# i think about isn't needed at all, becazuse we can just iterator the first 100 recent tweet and store the first
# tweet id as recent id for the next iteration in while loop. This way we can save our our api call search
# also, code will be less
# But there is still one problem, how to handle
# the keyword param in the case of the first iteration(should it be just, or hardcoded)
# we can do many things: for instance using the if condition is while loop with time etc.


def scrape_tweet():
    print("Hey! Welcome to the tweet scraper.")
    print("\nWhat do you wanna scrape today? (a hashtag or a keyword")
    print("\nIf it is a hashtag, you must prefix the word with the hashtag symbol")
    print("\ni.e for solar, you should type #solar")
    print("\n")
    word = input("Type the query: ")
    print("\n Nice! Let's do some more configuration then ")
    rwt = input("\nDo you wanna exclude the retweets in the query: ('y' or 'n') ")
    rply = input("\nDo you wanna exclude replies: ('y' or 'n') ")

    if rwt.lower() in ['y']:
        rwt = " -filter:retweets"
    else:
        rwt = ""

    if rply.lower() in ['y']:
        rply = " -filter:replies"
    else:
        rply = ""

    query = word + rwt + rply
    print(query)

    return query


def save_tweet_data(query, id_for_since):

    # search_word = "china -filter:retweets -filter:replies"
    cur = tweepy.Cursor(api.search_tweets, q=query, tweet_mode="extended", result_type="recent", count=100, since_id=id_for_since).items(100)
    print(cur)
    print(type(cur))


    # i think cursor is of return generator instead of list and hence we can only iterate over cursor once.
    # therefore above is not returning in anything, as there is nothing in cursor object
    # so what to do, either a copy of curosr object or use some logic to get the id

    # saving the data
    for index, tweet in enumerate(cur):
        print(tweet.full_text)

        if index == 0:
            # # change the since_id (as we will be using loop outside this function to fetch data for some peroid of time)
            temp_since_id = tweet.id
            print(temp_since_id)
    

        # trying different things here
        t = json.dumps(tweet._json)
        t = t + ",qseroiurewfijdei"

        with open('testing.txt', 'a') as f:
            try:
                f.write(t)
            except:
                print("\n\nwriting t")
                f.write(t)

        
    return temp_since_id

# save_tweet_data(temp_since_id)

t1 = time.time()
query = scrape_tweet()

# for finding the temporaray id (change this later with better logic)
# This has to be outside or some other logic has to be done!!!!!
# temp_search = api.search_tweets(q=query, tweet_mode='extended', count=100, result_type='recent')
# id_list = [tweet.id for tweet in temp_search]
# temp_since_id = id_list[-1]          # list start from newest id tweet first therefore, we wanna get the oldest as nothing will be returned.

temp_since_id = None
temp_since_id = save_tweet_data(query, temp_since_id)

"""
while True:

    temp_since_id = save_tweet_data(query, temp_since_id)

    print("Waiting for 10 seconds")
    t2 = time.time()
    time.sleep(10)

    # change this to 900 later
    if (t2-t1) > 30:
        break
        
"""