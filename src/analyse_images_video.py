### Code referenced from Google Cloud Video Intelligence API doc
### https://cloud.google.com/video-intelligence/docs/label-tutorial
import os
from google.cloud import videointelligence
import mysql_connection2
import datetime
import pymongo

def analyse (path):

    mydb = mysql_connection2.connect()
    mycursor = mydb.cursor()

    sql = "SELECT id FROM session ORDER BY id DESC LIMIT 1;"
    mycursor.execute(sql)
    res = mycursor.fetchall()
    # print("Fetch result:", result[0][0])

    myclient3 = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb3 = myclient3["twitter_db"]
    mycol3 = mydb3["session"]
    last_id = mycol3.find({},{ "_id": 1 }).sort("login_time")[mycol3.find().count()-1]["_id"]
    # myquery = {}
    # doc3 = { "session_id": "<TODO>", "frame_label_desc": frame_desc, "label_cat_desc": cat_desc, "frame_time_offset": frame_time_offset, "frame_confidence": frame_confidence, "login_time": str(datetime.datetime.now())}
    # x3 = mycol3.insert_one(doc)

    # print(x3.inserted_id, "MongoDB: Descriptor document inserted.")

    os.chdir(path)
    os.chdir("../")
    """Detect labels given a file path."""
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.enums.Feature.LABEL_DETECTION]

    with open('./twitter_images/vid.mp4', 'rb') as movie:
        input_content = movie.read()

    mode = videointelligence.enums.LabelDetectionMode.SHOT_AND_FRAME_MODE
    config = videointelligence.types.LabelDetectionConfig(label_detection_mode=mode)
    context = videointelligence.types.VideoContext(label_detection_config=config)

    operation = video_client.annotate_video(
        features=features, input_content=input_content, video_context=context)
    print ('\nProcessing video for label annotations:')
    print ('Please wait...')

    result = operation.result(timeout=90)
    print ('\nFinished processing.')

    # Process frame level label annotations
    frame_labels = result.annotation_results[0].frame_label_annotations
    frame_desc = ""

    for i, frame_label in enumerate(frame_labels):
        print('Frame label description: {}'.format(frame_label.entity.description))
        # print ('Frame label description: ' + frame_label.entity.description.encode('utf-8'))
        cat_desc = ""
        for category_entity in frame_label.category_entities:
            print('\tLabel category description: {}'.format(category_entity.description))
            cat_desc = '{}'.format(category_entity.description)

            # print ('\tLabel category description: ' + category_entity.description.encode('utf-8'))
        # Each frame_label_annotation has many frames,
        a=0
        frame_time_offset = ""
        frame_confidence = ""
        for frame in frame_label.frames:
            time_offset = (frame.time_offset.seconds +
                           frame.time_offset.nanos / 1e9)
            print ('\tframe time offset: {}s'.format(time_offset))
            print ('\tframe confidence: {}'.format(frame.confidence))
            print ('\n')
            a+=1
            frame_time_offset = frame_time_offset + str(time_offset) + " "
            frame_confidence = frame_confidence + str(frame.confidence)[:4] + " "

        frame_desc = '{}'.format(frame_label.entity.description)

        mydb = mysql_connection2.connect()
        mycursor = mydb.cursor()
        sql2 = "INSERT INTO descriptor (session_id, frame_label_desc, label_cat_desc, frame_time_offset, frame_confidence, login_time) VALUES (%s, %s, %s, %s, %s, %s);"
        val2 = (res[0][0], frame_desc, cat_desc, frame_time_offset, frame_confidence, str(datetime.datetime.now()))
        mycursor.execute(sql2, val2)

        mydb.commit()

        print(mycursor.rowcount, "Descriptor record inserted.")

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["twitter_db"]
        mycol = mydb["descriptor"]
        doc = { "session_id": last_id, "frame_label_desc": frame_desc, "label_cat_desc": cat_desc, "frame_time_offset": frame_time_offset, "frame_confidence": frame_confidence, "login_time": str(datetime.datetime.now())}
        x = mycol.insert_one(doc)

        print(x.inserted_id, "MongoDB: Descriptor document inserted.")
