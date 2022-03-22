import psycopg2 as pg2

database ="dvdrental"
password = "123456"
username = "postgres"

try: 
	conn = pg2.connect(
			dbname= database,
			user= username,
			password = password,			
		)
	print("Connected")

	# make cursor
	cur = conn.cursor()

	# query
	cur.execute("SELECT * FROM payment")

	# fetch one
	for i in cur.fetchmany(10):
		print(i)

	# close connectione
	conn.close()
except Exception as e:
	print(e)


