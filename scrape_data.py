
# This program scrapes the data from twitter

import tweepy
from dotenv import load_dotenv
import os
from pprint import pprint
import json

load_dotenv()

consumer_key = os.getenv("API_Key")
consumer_secret = os.getenv("API_Secret_key")
access_token = os.getenv("Access_Token")
access_token_secret = os.getenv("Access_Token_Secret")

print("Hello world")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)




limit = api.rate_limit_status()
print(limit["resources"]["search"])

limit = json.dumps(limit, indent=4)       # dict to json
with open("testing.json", "w") as f:
	f.write(limit)















############################## GETTING DATA ###############################




search = api.search_tweets(q="elon musk", count=100, tweet_mode="extended")
for tweet in search:
	print(tweet.full_text)

	tweet = json.dumps(tweet._json, indent=4)

	with open('testing.json', 'w') as f:
		f.write(tweet)