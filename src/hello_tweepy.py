import tweepy
import twitter_credentials
import json
import os
import urllib
import shutil
import subprocess

auth = tweepy.OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
media_urls = []
for tweet in public_tweets:
    #get json(its in unicode) from status and access as dictionary
    json_dict = tweet._json
    #reading the media object from the entities and extended entities object
    media_list=[]
    #TODO improve this logic as its not getting all images and skipping tweets I think
    if(json_dict.get("entities").get("media")!=None):
        media_list = json_dict.get("entities").get("media")
    elif(json_dict.get("extended_entities")!=None):
        media_list = json_dict.get("extended_entities").get("media")
    #iterating through the media object to look for photos and add media_url to list
    for media in media_list:
        if(media.get("type") == "photo"):
            media_urls.append(media.get("media_url"))

if(len(media_urls)>0):
    print("Images received from Twitter.\n")

#New path for downloading images to
curr_path = os.getcwd()
new_path = curr_path + '/twitter_images'
path_made = False
if not os.path.exists(curr_path+"/twitter_images"):
    print "Creating path for images\n"
    os.makedirs(new_path)
    path_made = True
else:
    print "Path already exists. Please Delete before proceeding\n"

#data_%03i.dat" % i
#filename = 'data_%d.dat'%(i,)

#If required path is made. Download images from media_urls list
if(path_made):
    os.chdir(new_path)
    i=0
    print "Downloading Twitter images"
    for img in media_urls:
        urllib.urlretrieve(img, "img_%03i.jpg"%i)
        i=i+1

#Attempting the FFMPEG module integration

#for command line
#ffmpeg -r 1 -i img_%03d.jpg -vcodec mpeg4 -y movie.mp4
code=subprocess.call(['ffmpeg', '-r', '1', '-i', 'img_%03d.jpg', '-vcodec', 'mpeg4', '-y', 'vid.mp4'])
print ('Video Process:',code,'\n')
