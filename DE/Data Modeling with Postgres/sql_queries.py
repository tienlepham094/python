# create table
songplays_create = ('''
	CREATE TABLE IF NOT EXISTS songplays(
		songplay_id VARCHAR(50) SERIAL PRIMARY KEY,
		start_time TIMESTAMP,
		user_id INTEGER,
		level VARCHAR(25) NOT NULL,
		song_id VARCHAR(50),
		artist_id VARCHAR(50),
		session_id INTEGER NOT NULL,
		location VARCHAR(50) NOT NULL,
		user_agent VARCHAR(50) NOT NULL
	)
''')

users_create = ('''
	CREATE TABLE IF NOT EXISTS users(
		user_id INTEGER PRIMARY KEY,
		first_name VARCHAR(50),
		last_name VARCHAR(50),
		gender VARCHAR(10),
		level VARCHAR(25) NOT NULL
	)
''')

artists_create = ('''
	CREATE TABLE IF NOT EXISTS artists(
		artist_id VARCHAR(50) PRIMARY KEY,
		name VARCHAR(50),
		location VARCHAR(50) NOT NULL,
		latitude VARCHAR(50) NOT NULL,
		longitude VARCHAR(50) NOT NULL
	)
''')

time_create = ('''
	CREATE TABLE IF NOT EXISTS time(
		start_time TIMESTAMP PRIMARY KEY,
		hour INTEGER,
		day INTEGER ,
		week INTEGER ,
		year INTEGER ,
		weekday INTEGER VARCHAR(25)
	)
''')

songs_create = ('''
	CREATE TABLE IF NOT EXISTS songs(
		song_id VARCHAR(50) PRIMARY KEY,
		title VARCHAR(50),
		artist_id VARCHAR(50),
		year INTEGER,
		duration NUMERIC,
	)
''')