import random
import numpy

if __name__ == "__main__":
    # Default random method get one number ( float ) between 0 and 1
    print("Random Number between 0 and 1 [Default] -> ", random.random(), "\n")

    # Random method get one int number between specified interval ex. 1 - 100
    # Includes endpoints
    print("Random Number between 1 and 100 -> ", random.randint(1, 100), "\n")

    # Generate a random number within a range by specifying the increment.
    # It produces a random number from an exclusive range.
    # If step is specified, generated number must be multiple of step value
    print("Random Number in range with step", random.randrange(1, 100, 20), "\n")

    # Generate 5 x 3 matrix of random ints
    matrix = numpy.random.randint(1, 100, size=(5, 3))
    print("Random matrix 5 x 3\n", "->\t", matrix, "\n")

    # Generate a shuffle list
    int_list = [3, 5, 6, 10, 11, 7]
    shuffle_list = int_list.copy()
    random.shuffle(shuffle_list)
    print("Random shuffle list: ", "Before-> ", int_list, "\t", "After ->", shuffle_list, "\n")

    # The random.choices() return a k sized list of elements chosen from the population with replacement
    # weights or cum_weights are used to define the selection probability for each element
    # If a weights sequence is specified, random selections are made according to the relative weights
    # Alternatively, if a cum_weights sequence is given,
    # the random selections are made according to the cumulative weights
    # If neither weights nor cum_weights are specified, selections are made with equal probability
    # You cannot specify both weights and cumulative weights.
    int_list = [151, 251, 351, 451, 551]
    print("Random choice with weight probability ->", random.choices(int_list, weights=(10, 20, 30, 40, 50), k=2), "\n")
