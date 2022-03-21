import mysql.connector
from datetime import datetime

# connect to mysql
db = mysql.connector.connect(
 	host= "localhost",
 	user ="root",
 	password="123456",
 	database="testdatabase")

# make a cursor obj
mycursor = db.cursor()

# create table
mycursor.execute("CREATE TABLE test(id SMALLINT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50) NOT NULL, gender ENUM('M', 'F') NOT NULL, created DATETIME NOT NULL)")

# insert value into table
mycursor.execute("INSERT INTO test(name,created,gender) VALUES (%s,%s,%s)",("Joe", datetime.now(), "M"))
# commit to database
db.commit()


# print the column with condition
mycursor.execute("SELECT * FROM test WHERE gender ='M' ORDER BY id DESC")

for i in mycursor:
	print(i)

# alter table
mycursor.execute("ALTER TABLE test ADD COLUMN address VARCHAR(50) NOT NULL")

# fetch all
mycursor.execute("SELECT * FROM test")
myresult = mycursor.fetchall()

for i in myresult:
	print(i)

#fetch one
mycursor.execute("DESCRIBE test")
print(mycursor.fetchone())