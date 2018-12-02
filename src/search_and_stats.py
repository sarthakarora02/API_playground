import mysql_connection2
import pymongo
import numpy as np
import matplotlib.pyplot as plt


def search_fn_mysql(query):
    mydb = mysql_connection2.connect()
    mycursor = mydb.cursor()

    sql1 = "SELECT session_id FROM descriptor WHERE frame_label_desc = (%s) OR label_cat_desc = (%s);"
    val1 = (query, query,)

    mycursor.execute(sql1, val1)
    myresult = set(mycursor.fetchall())

    myresult3 = set()
    for m in sorted(myresult):
        sql3 = "SELECT twitter_handle FROM session WHERE id = (%s);"
        val3 = (m[0],)
        mycursor.execute(sql3, val3)
        myresult3 = myresult3 | set(mycursor.fetchall())

    print("Users which have "+query+" in MySQL db")
    for user in sorted(myresult3):
        print(user[0])

def search_fn_mongodb(query):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["twitter_db"]
    mycol1 = mydb["session"]
    mycol2 = mydb["descriptor"]

    fetch_res = mycol2.find({ '$or': [ { "frame_label_desc": query }, { "label_cat_desc": query } ] },{ "session_id": 1 })
    fetch_res2 = []
    for x in fetch_res:
        for y in mycol1.find({ "_id": x['session_id'] },{ "twitter_handle": 1 }):
            fetch_res2.append(y['twitter_handle'])

    print("Users which have "+query+" in MongoDB")
    for user in sorted(list(set(fetch_res2))):
        print(user)

def stat_mysql():
    mydb = mysql_connection2.connect()
    mycursor = mydb.cursor()

    sql1 = "SELECT twitter_handle, num_images FROM session;"

    mycursor.execute(sql1)
    myresult = mycursor.fetchall()

    handles = []
    imgs = []
    for x in myresult:
        handles.append(x[0])
        imgs.append(x[1])

    handles = tuple(handles)
    y_pos = np.arange(len(handles))
    print(handles)
    print(imgs)
    plt.barh(y_pos, imgs, align='center', alpha=0.5)
    plt.yticks(y_pos, handles)
    plt.xlabel('Images')
    plt.ylabel('Twitter Handles')
    plt.title('MySQL: Images per feed')

    plt.show()

def stat_mongodb():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["twitter_db"]
    mycol1 = mydb["session"]
    fetch_res = mycol1.find({},{ "twitter_handle": 1 , "num_images": 1 })
    handles = []
    imgs = []
    for x in fetch_res:
        handles.append(x['twitter_handle'])
        imgs.append(int(x['num_images']))

    handles = tuple(handles)
    y_pos = np.arange(len(handles))
    print(handles)
    print(imgs)
    x_pos = np.arange(len(imgs))
    plt.barh(y_pos, imgs, align='center', alpha=0.5)
    plt.yticks(y_pos, handles)
    # plt.xticks(x_pos, imgs)
    plt.xlabel('Images')
    plt.ylabel('Twitter Handles')
    plt.title('MongoDB: Images per feed')

    plt.show()



if __name__ == "__main__":
    db = input("[1] MySQL    [2] MongoDB: ")
    operation = input("[a] Search    [b] Statistics: ")
    if db == '1' and operation == 'a':
        search_fn_mysql(query)
    elif db == '2' and operation == 'a':
        search_fn_mongodb(query)
    elif db == '1' and operation == 'b':
        stat_mysql()
    elif db == '2' and operation == 'b':
        stat_mongodb()
