import tweepy
import twitter_credentials

auth = tweepy.OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
