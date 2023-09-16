import threading


def print_hello(name, surname):
    print("Hello There", name, surname)


if __name__ == "__main__":
    # Returns the list of alive thread objects
    print(threading.active_count())

    # Return the current thread object
    print(threading.current_thread())

    # Return a complete list of thread objects that are currently active
    print(threading.enumerate())

    # Return the main thread
    print(threading.main_thread())

    # Return the stack size utilized when creating new threads
    print(threading.stack_size())

    thread1 = threading.Thread(target=print_hello("name", "surname"))
    thread1.start()

    thread2 = threading.Thread(target=print_hello("name2", "surname2"))
    thread2.start()

    # this ensures that End of main thread will be printed only after thread1 finished
    # Otherwise, the compiler will choices what run
    thread1.join()
    thread2.join()
    print("End of main thread")

