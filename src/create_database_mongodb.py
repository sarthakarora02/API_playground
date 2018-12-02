import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["dbtest"]

mycol1 = mydb["mycol1"]
mycol2 = mydb["mycol2"]

doc1 = { "twitter_handle": "twitter_handle", "num_images": "image_num", "img_path": "./twitter_images", "vid_path": "./twitter_images", "login_time": "str(datetime.datetime.now())"}
x1 = mycol1.insert_one(doc1)

doc2 = { "session_id": "last_id", "frame_label_desc": "frame_desc", "label_cat_desc": "cat_desc", "frame_time_offset": "frame_time_offset", "frame_confidence": "frame_confidence", "login_time": "str(datetime.datetime.now())"}
x2 = mycol2.insert_one(doc2)
