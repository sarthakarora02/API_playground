import get_images
import make_video

if __name__ == "__main__":
    img_path = get_images.read_twitter()
    print("OUTPUT " + str(img_path))
    if(img_path!=0):
        print "Twitter images downloaded ./twitter_images"
        val = make_video.make_vid(img_path)
        if (val==1):
            ans = analyse_images_video.analyse(img_path)
        else:
    else:
        print "Error occurred in fetching data from Twitter"
