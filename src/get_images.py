import tweepy
import twitter_credentials
import json
import os
import urllib
import shutil

def read_twitter(twitter_handle, image_num):
    auth = tweepy.OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
    auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_secret)

    api = tweepy.API(auth)

    try:
        #public_tweets = api.home_timeline()
        user_tweets = api.user_timeline(screen_name = twitter_handle, count = 200, tweet_mode = 'extended')
    except:
        print "Invalid Twitter handle. Rerun with correct screen name"
        return 0

    media_urls = []

    if(len(user_tweets)>0):
        #print str(len(public_tweets))+" Statuses"
        num = int(image_num)
        for tweet in user_tweets:
            #get json(its in unicode) from status and access as dictionary
            json_dict = tweet._json
            #reading the media object from the entities and extended entities object
            #print json.dumps(json_dict, indent = 4)
            #print "\n"
            media_list=[]
            if(json_dict.get("entities").get("media")!=None):
                media_list = json_dict.get("entities").get("media")
            elif(json_dict.get("entities").get("media")!=None and json_dict.get("extended_entities")!=None):
                media_list = json_dict.get("extended_entities").get("media")
            #iterating through the media object to look for photos and add media_url to list
            for media in media_list:
                if(media.get("type") == "photo" and num!=0):
                    media_urls.append(media.get("media_url"))
                    num-=1

        if(len(media_urls)>0):
            print(str(len(media_urls))+" Images received from Twitter.\n")
            #New path for downloading images to
            curr_path = os.getcwd()
            new_path = curr_path + '/twitter_images'
            path_made = False
            if not os.path.exists(curr_path+"/twitter_images"):
                print "Creating path for images\n"
                os.makedirs(new_path)
                path_made = True
            else:
                print "Path already exists. Please Delete ./twitter images before proceeding\n"
                return 0

            #If required path is made. Download images from media_urls list
            if(path_made):
                os.chdir(new_path)
                i=0
                print "Downloading Twitter images to ./twitter_images"
                for img in media_urls:
                    urllib.urlretrieve(img, "img_%05i.jpg"%i)
                    i=i+1
                return new_path
            else:
                "Path couldn't be created. Try again.\n"
                return 0
        else:
                print("No images received. Try again.\n")
                return 0

    else:
        print "No tweets in "+ twitter_handle +"\'s Timeline"
        return 0
