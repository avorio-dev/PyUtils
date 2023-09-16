import re

if __name__ == "__main__":
    # Six most important sequence characters in regex building are:

    # \d: Matches any decimal digit.
    #   This is really the same as writing [0-9] but is done so often that it has its own shortcut sequence.

    # \D: Matches any non-decimal digit.
    #   This is the set of all characters that are not in [0-9] and can be written as [^0-9].

    # \s: Matches any white space character.
    #   White space is normally defined as a space, carriage return, tab, and non-printable character.
    #   Basically, white space is what separates words in a given sentence.

    # \S: Matches any non-white space character.
    #   This is simply the inverse of the \s sequence.

    # \w: Matches any alphanumeric character.
    #   This is the set of all letters and numbers in both lower and uppercase.

    # \W: Matches any non-alphanumeric character.
    #   This is the inverse of the \w sequence.

    text = "Hello my name is Lyon"
    print("text -> \t", text)
    print("Find all 'Lyon': \t", re.findall(r"Lyon", text), "\n")

    text = "Hello I live on lane 8 which is near street 42"
    print("text -> \t", text)
    print("Find all digits: \t", re.findall(r"\d", text), "\n")

    text = ("Hello I live on lane 8 which is near street 42, now all digit will be found and not only the first"
            "So instead of 4 will be found 42")
    print("text -> \t", text)
    print("Find all digits: \t", re.findall(r"\d+", text), "\n")

    text = "Hello my name is Lyon and it will be searched in this string"
    print("text -> \t", text)
    if re.search("Lyon", text):
        print("Found 'Lyon' \n")

    text = "I will be split at % in two string"
    print("text -> \t", text)
    split_text = re.split(r'%', text)
    print("Split Result: \t", split_text, "\n")

    # Regex for find email in long text
    mail_regex = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}"
    text = "My email is: myemail@gmail.com"
    print("text -> \t", text)
    print("Mail found: \t", re.findall(mail_regex, text), "\n")
