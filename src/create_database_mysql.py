import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE dbtest")
mycursor.execute("USE dbtest")

mycursor.execute("CREATE TABLE mytbl1 (id INT AUTO_INCREMENT PRIMARY KEY, twitter_handle VARCHAR(20), num_images INT, img_path VARCHAR(100), vid_path VARCHAR(100), login_time DATETIME)")
mycursor.execute("CREATE TABLE mytbl2 (id INT AUTO_INCREMENT PRIMARY KEY, session_id INT, frame_label_desc VARCHAR(100), label_cat_desc VARCHAR(100), frame_time_offset VARCHAR(1000), frame_confidence VARCHAR(1000), login_time DATETIME)")
