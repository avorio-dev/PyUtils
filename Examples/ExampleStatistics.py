import statistics

if __name__ == "__main__":

    # Initial Dataset
    scores = [6, 7, 2, 6, 3, 5, 5, 5, 2, 6, 1, 2, 4, 1, 4, 10, 11, 100, 1000, 1000]
    print("Initial Score -> ", scores)

    # Mean
    print("Mean:\t", statistics.mean(scores), "\n",
          "The average of a set of numbers. Add up all numbers in the set,", "\n",
          "and then divide that total by the number of numbers in the set to find the mean.", "\n")

    # Median
    print("Median:\t", statistics.median(scores), "\n",
          "The middle number, or midpoint of the data, when the numbers are listed in ascending order.", "\n")

    # Mode
    print("Mode:\t", statistics.mode(scores), "\n",
          "The mode is the value that occurs most often.", "\n")

    # Low Median
    print("Low Median: \t", statistics.median_low(scores), "\n",
          "The low median is the value from the data points", "\n",
          "that is just lower than the actual median of the data.", "\n")

    # High Median
    print("Low Median: \t", statistics.median_high(scores), "\n",
          "The high median is the value that is just higher than the actual median.", "\n")

    # Variance
    scores_mean = statistics.mean(scores)
    print("Variance: ", statistics.variance(scores, scores_mean), "\n",
          "Variance in statistics refers to the average of the squared differences from the mean.", "\n",
          "A variance value of zero means that all of the data values are identical", "\n")

    # Standard Deviation
    scores_mean = statistics.mean(scores)
    print("Standard Deviation: ", statistics.stdev(scores), "\n",
          "Standard deviation is used to show how much variation from the mean exists.", "\n",
          "You can think of it as a typical deviation from the mean.", "\n",
          "A low standard deviation indicates that the values tend to be close to the mean of the set,", "\n",
          "while a high standard deviation indicates that the values are spread out over a wider range", "\n")
