import os
from dotenv import load_dotenv
import tweepy

load_dotenv()

twitter_api_key = os.getenv("twitter_api_key", default="OOPS")
twitter_api_secret = os.getenv("twitter_api_secret", default="OOPS")
twitter_access_token = os.getenv("twitter_access_token", default="OOPS")
twitter_access_token_secret = os.getenv("twitter_access_token_secret", default="OOPS")

auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
print(type(auth))
auth.set_access_token(twitter_access_token, twitter_access_token_secret)

client = tweepy.API(auth)
print(type(client))
#print(dir(client))
#print("----------")

#public_tweets = client.home_timeline()
#for tweet in public_tweets:
 #   print(type(tweet), tweet.text)

print("----------")

elon_tweets = client.user_timeline("elonmusk", tweet_mode = "extended")

for tweet in elon_tweets:
    print(type(tweet), tweet.full_text)
