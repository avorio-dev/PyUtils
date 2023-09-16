if __name__ == "__main__":
    # Syntax Error:
    # Error caused by not following the proper structure (syntax) of the language
    # is called syntax error or parsing error.
    # These errors are usually indicated by a little upward arrow in Python, as shown in the code snippet below.",
    # >>> if x < 5
    #  File <input>
    #       if x < 5
    #             ^
    #       SyntaxError: invalid syntax"

    # By handling exceptions,
    # you can provide an alternative flow of execution to avoid crashing your program unexpectedly.

    # Wil crash -> print(language) so we will use try catch,
    try:
        print(language)
    except NameError as e:
        print("Not defined variable")
    finally:
        language = "Python"
        print(language)

    # Raise Error will stop the program
    def print_five_items(data):
        if len(data) != 5:
            raise ValueError("The argument must have five elements")
        for item in data:
            print(item)


    print_five_items([5, 2])
