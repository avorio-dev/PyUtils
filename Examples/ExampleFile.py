if __name__ == "__main__":
    """
        “r” – Read mode is used only to read data from the file. It is also the default mode.
        
        “w” – It will create a new file if it does not exist, 
                otherwise will overwrite the file and allow you to write to it.
        
        “a” – It will write data to the end of the file. 
                It does not erase the existing data, and the file must exist for this mode.
        
        “r+” – It opens the file to read and write both. 
                The file pointer will be at the beginning of the file.
        
        “w+” – The exact same as r+ but if the file does not exist, a new one is made. 
                Otherwise, the file is overwritten.
        
        “a+” – Similar to w+ as it will create a new file if the file does not exist. 
                Otherwise, the file pointer is at the end of the file if it exists.
    """

    print("Reading Example\n")

    path = 'FileRead.txt'

    file_handler = open(path, "r")
    content = file_handler.read()
    print("-> read")
    print(content, "\n")
    file_handler.close()

    file_handler = open(path, "r")
    content = file_handler.readline()
    print("-> Read Line")
    print(content, "\n")
    file_handler.close()

    file_handler = open(path, "r")
    content = file_handler.readlines()
    print("-> Read Lines")
    print(content, "\n")
    file_handler.close()

