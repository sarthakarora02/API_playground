import get_images
import make_video
import analyse_images_video
import sys
import mysql_connection2
import datetime
import pymongo

if __name__ == "__main__":

    twitter_handle = input("Enter twitter handle: ")
    image_num = input("Enter the number of images you would like to use: ")
    img_path = ""

    mydb = mysql_connection2.connect()
    mycursor = mydb.cursor()

    sql = "INSERT INTO session (twitter_handle, num_images, img_path, vid_path, login_time) VALUES (%s, %s, %s, %s, %s);"
    val = (twitter_handle, int(image_num), "./twitter_images", "./twitter_images", str(datetime.datetime.now()))
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "MySQL: Session record inserted.")

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["twitter_db"]
    mycol = mydb["session"]
    doc = { "twitter_handle": twitter_handle, "num_images": image_num, "img_path": "./twitter_images", "vid_path": "./twitter_images", "login_time": str(datetime.datetime.now())}
    x = mycol.insert_one(doc)

    print(x.inserted_id, "MongoDB: Session document inserted.")

    try:
        num = int(image_num)
        if(num>0):
            img_path = get_images.read_twitter(twitter_handle, image_num)
        else:
            print ("Number <= 0. Please enter a positive integer")
            exit()
    except ValueError:
       print("Please enter an integer")
       exit()

    print("Path to images " + str(img_path))
    if(img_path!=0):
        print ("Twitter images downloaded to ./twitter_images")
        val = make_video.make_vid(img_path)
        if (val==1):
            ans = analyse_images_video.analyse(img_path)
        else:
            print ("Video not obtained.")
    else:
        print ("Error occurred in fetching data from Twitter")
