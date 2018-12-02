import mysql_connection2
import pymongo


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

if __name__ == "__main__":
    query = input("Search for: ")
    db = input("[1] MySQL    [2] MongoDB: ")
    if db == '1':
        search_fn_mysql(query)
    elif db == '2':
        search_fn_mongodb(query)
