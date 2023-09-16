import time

if __name__ == "__main__":
    # The Python time() function retrieves the current time.
    # The time is represented as the number of seconds since January 1, 1970.
    epoch_time = time.time()

    print("Actual Timestamp in millis from 01.01.1970: \t", epoch_time, "\n")

    # Get current time in local format
    local_time = time.ctime(epoch_time)
    print("Local Time: \t", local_time, "\n")
