import tweepy
import twitter_credentials
import json

auth = tweepy.OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
media_urls = []
for tweet in public_tweets:
    #get json(its in unicode) from status and access as dictionary
    json_dict = tweet._json
    #reading the media object from the entities
    media_list = json_dict.get("entities").get("media")
    #iterating through the media object to look for photos and add media_url to list
    for media in media_list:
        if(media.get("type") == "photo"):
            media_urls.append(media.get("media_url"))
print media_urls
