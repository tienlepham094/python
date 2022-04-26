import psycopg2
from sql_queries import create_table_query

def create_database():
	try: 
		conn = psycopg2.connect(dbname="song", user="postgres", password="123456")
		conn.set_session(autocommit=True)
		cur = conn.cursor()

		return cur, conn
	except psycopg2.Error as e:
		print(e)


def create_tables(cur,conn):
	for query in create_table_query:
		cur.execute(query)
		conn.commit()

def main():
	cur, conn = create_database()
	create_tables(cur,conn)
	conn.close()

if __name__ == "__main__":
	main()
