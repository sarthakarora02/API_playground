# 601_Mini_project_APIs
EC 601 Mini Project- A python project that downloads images from a particular twitter handle, converts them to a video and 
uses Google's Video Intelligence API to describe the content of the video. Databse Integration includes MySQL and MongoDB

## Built using

* Python 3.6.6 
* Tweepy 3.6.0
* FFMPEG version 4.0.2
* google-cloud-videointelligence 1.3.0

## Paths

* Path to images ./twitter_images
* Path to video ./twitter_images/vid.mp4

## User Guide

* Run using: python main.py
* images from twitter are stored in the format: img_%05d.jpg

## Scripts

### search_and_stats.py 
* Search for descriptor/label and view corresponding list of handles
* Bar chart for Images per feed/handle
* View most occurring descriptor

### make_video.py 
* Use ffmpeg to get video of images

### analyse_images_video.py 
* Run video intelligence API over the video to get labels
* Store labels in databases(MySQL and MongoDB)

### create_database_mongodb.py and create_database_mysql.py
* Database and Table/Collection creation

## Example Output

601_Mini_project_APIs/src/Screen Shot 2018-09-18 at 11.02.56 PM.png

## References

* Google Cloud Video Intelligence API python Frame level and video level example referred from https://cloud.google.com/video-intelligence/docs/label-tutorial
* README Template referred from https://gist.githubusercontent.com/PurpleBooth/109311bb0361f32d87a2/raw/8254b53ab8dcb18afc64287aaddd9e5b6059f880/README-Template.md 

