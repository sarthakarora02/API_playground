import get_images
import make_video

if __name__ == "__main__":
    img_path = get_images.read_twitter()
    print("OUTPUT " + str(ans))
    if(img_path!=0):
        print "Twitter images downloaded ./twitter_images"
        ans = make_video.make_vid(img_path)
        print "Video O/p: "+str(ans)
    else:
        print "Error occurred"
