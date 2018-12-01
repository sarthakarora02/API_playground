import mysql_connection2


def search_fn(query):
    mydb = mysql_connection2.connect()
    mycursor = mydb.cursor()

    sql1 = "SELECT session_id FROM descriptor WHERE frame_label_desc = (%s);"
    val1 = (query,)

    sql2 = "SELECT session_id FROM descriptor WHERE label_cat_desc = (%s);"
    val2 = (query,)

    mycursor.execute(sql1, val1)
    myresult1 = set(mycursor.fetchall())

    mycursor.execute(sql2, val2)
    myresult2 = set(mycursor.fetchall())

    myresult = myresult1 | myresult2

    myresult3 = set()
    for m in sorted(myresult):
        sql3 = "SELECT twitter_handle FROM session WHERE id = (%s);"
        val3 = (m[0],)
        mycursor.execute(sql3, val3)
        myresult3 = myresult3 | set(mycursor.fetchall())

    print("Users which have "+query)
    for user in sorted(myresult3):
        print(user[0])

if __name__ == "__main__":
    query = input("Search for: ")
    search_fn(query)
