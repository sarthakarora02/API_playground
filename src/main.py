import get_images
import make_video
import analyse_images_video
import sys

if __name__ == "__main__":

    twitter_handle = raw_input("Enter twitter handle: ")
    img_path = get_images.read_twitter(twitter_handle)
    print("Path to images " + str(img_path))
    if(img_path!=0):
        print "Twitter images downloaded to ./twitter_images"
        val = make_video.make_vid(img_path)
        if (val==1):
            ans = analyse_images_video.analyse(img_path)
        else:
            print "Video not obtained."
    else:
        print "Error occurred in fetching data from Twitter"
