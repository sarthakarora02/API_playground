import tweepy
import twitter_credentials
import json

auth = tweepy.OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

#get json(its in unicode) from status and access as dictionary
json_unicode = public_tweets[0]._json
print(json_unicode.get("entities"))
