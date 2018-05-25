from pyspark import SparkConf, SparkContext

def loadMovienames():
    movieNames = {}
    with open("ml-100k/u.item") as f:
        for line in f:
            fields = line.split('|')
            movieNames[int(fields[0])] = fields[1]
        return movieNames

def parseInput(line):
    fields = line.split()
    return (int(fields[1]), (float(fields[2]), 1.0))

if __name__ = "__main__":
    conf = SparkConf().setAppName("WorstMovies")
    sc = SparkContext(conf = conf)

    movieNames = loadMovieNames()

    lines = sc.textFile("hdfs:///user/maria_dev/ml-100k/u.data")

    # convert to (movieID, (rating, 1.0))
    movieRatings = line.map(parseInput)

    # reduce to (movieID, (sumOfRatings, totalRatings))
    ratingsTotalsandCount = movieRatings.reduceBykey(lambda movie1, movie2: (movie1[0] + movie2[1]))

    # Map to (movieID, averageRating)
    averageRatings = ratingsTotalsandCount.mapValue(lambda totalandCount : totalandCount[0]/totalandCount[1])

    # Sort by average rating
    sortedMovies = averageRatings.sortBy(lambda x: x[1])

    # take the top 10
    results = sortedMovies.take(10)

    #print
