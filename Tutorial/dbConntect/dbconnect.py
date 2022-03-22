import mysql.connector

db = mysql.connector.connect(
	host="localhost",
	user ="root",
	password="123456",
	database="testdatabase"
	)

mycursor = db.cursor()

 #create database
# mycursor.execute("CREATE DATABASE testdatabase")

# CREATE table
mycursor.execute("CREATE TABLE person( name VARCHAR(50), age SMALLINT UNSIGNED, person_id INT PRIMARY KEY)")

# show person table
mycursor.execute("DESCRIBE person")
for i in mycursor:
		print(i)

#insert into table
mycursor.execute("INSERT INTO person(name, age, person_id) VALUES ('John', 45, 1)")

db.commit()

# select table
mycursor.execute("SELECT * FROM person")
for x in mycursor:
	print(x)