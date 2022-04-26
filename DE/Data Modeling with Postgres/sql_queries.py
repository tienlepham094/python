
# create table
songplays_create = ('''
	CREATE TABLE IF NOT EXISTS songplays(
		songplay_id SERIAL PRIMARY KEY,
		start_time TIME ,
		user_id INTEGER ,
		level VARCHAR(255) NOT NULL,
		song_id VARCHAR(255),
		artist_id VARCHAR(50),
		session_id INTEGER ,
		location VARCHAR(255) ,
		user_agent VARCHAR(255) 
	)
''')

users_create = ('''
	CREATE TABLE IF NOT EXISTS users(
		user_id INTEGER PRIMARY KEY,
		first_name VARCHAR(255),
		last_name VARCHAR(255),
		gender VARCHAR(255),
		level VARCHAR(255) NOT NULL
	)
''')

artists_create = ('''
	CREATE TABLE IF NOT EXISTS artists(
		artist_id VARCHAR(255) PRIMARY KEY,
		name VARCHAR(255),
		location VARCHAR(255) NOT NULL,
		latitude VARCHAR(255) NOT NULL,
		longitude VARCHAR(255) NOT NULL
	)
''')

time_create = ('''
	CREATE TABLE IF NOT EXISTS time(
		start_time TIME PRIMARY KEY,
		hour INTEGER,
		day INTEGER ,
		week INTEGER ,
		month INTEGER,
		year INTEGER ,
		weekday INTEGER
	)
''')

songs_create = ('''
	CREATE TABLE IF NOT EXISTS songs(
		song_id VARCHAR(255) PRIMARY KEY,
		title VARCHAR(255),
		artist_id VARCHAR(255),
		year INTEGER,
		duration NUMERIC
	)
''')
# insert table
songplay_insert = """ INSERT INTO songplays (start_time, user_id,
                        level, song_id, artist_id, session_id, location, user_agent)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        """

user_insert = """ INSERT INTO users (user_id, first_name, last_name, gender, level)
                    VALUES (%s, %s, %s, %s, %s)
                    """

songs_insert = """ INSERT INTO songs  (song_id, title, artist_id, year, duration)
                    VALUES (%s, %s, %s, %s, %s)"""

artist_insert = """ INSERT INTO artists  (artist_id, name, location, latitude, longitude)
                    VALUES (%s, %s, %s, %s, %s)"""


time_insert = """ INSERT INTO time (start_time, hour, day, week, month, year, weekday)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """

insert_table_query=[songplay_insert, user_insert, songs_insert, artist_insert, time_insert]
create_table_query =[songplays_create, users_create, artists_create, time_create, songs_create]
