import findspark
findspark.init()
from pyspark import SparkConf, SparkContext



# this function just creates a Python "dictionary" we can later
# use to convert movie's ID to movie names whill printong out
# the final result

def loadMovieNames():
	movieNames = {}
	with open('ml-100/u.item') as f:
		for line in f:
			fields = line.split('|')
			movieNames[int(fields[0])] = fields[1]
	return movieNames

# Take each line of u.data and convert it to (movieId, (rating, 1.0))
# This way we can then add up all the ratings for each movie

def parseInput(line):
	fields = line.split()
	return (int(fields[1]), (float(fields[2]), 1.0))

if __name__ ="__main__":
	conf = SparkConf().setAppName("WorstMovies")
	sc = SparkContext(conf = conf)

	#load up movie ID -> movie name lookup table
	movieNames = loadMovieNames()

	#load up the raw u.data file
	lines = sc.textFile('hdfs://user/maria_dev/ml-100k/u.data')

	#convert to (movieId, (rating, 1.0))
	movieRatings = lines.map(parseInput)

	#reduce to (movieID, (sumOfRatings, totalRatings))
	ratingTotalsAndCount = movieRatings.reduceByKey(lambda movie1, movie2:
		(movie1[0]+ movie2[0]))

	# Map to (movieId, averageRating)
	averageRatings = ratingTotalsAndCount.mapValues(lambda totalAndCount: totalAndCount[0]/
		totalAndCount[1])

	#sort by average rating
	sortedMovies = averageRatings.sortBy(lambda x: x[1])

	#take the top 10 results
	results = sortedMovies.take(10)

	#print them out:
	for result in results:
		print(movieNames[result[0]], result[1])