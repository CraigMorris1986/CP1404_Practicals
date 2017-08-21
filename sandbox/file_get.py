# This is an example of file retrieval in python.
FILE_PATH = "test_write.txt"


def file_read():
    in_file = open(FILE_PATH, "r")  # This 'unpacks' the file/contents into a python variable (object)

    print(in_file.read()) # This will display 'unpacked' file contents through the variable.

    file_content = in_file.read() # This 'saves' the files 'unpacked' read contents into a variable without needing to
    # the .read() function every time.

    print(type(in_file))

    print(repr(file_content))  # The repr() function prints the files content through the variable in a RAW format
                               # (\n etc)

    print(file_content) # This will display 'unpacked' file contents through the saved variable. Doesn't need to
    # unpack again using processor power to use the .read() function again.

    in_file.close() # This closes the file. MUST ALWAYS close the file after its finished its use!


def file_write():
    in_file = open(FILE_PATH, "w")
    user_written_input = str(input("Please input a string : ")).capitalize()
    print(user_written_input, file=in_file)
    print("<{}> was entered into {} file".format(user_written_input, FILE_PATH))
    in_file.close()


def file_append():
    in_file = open(FILE_PATH, "a")  # appends to new line in file.
    user_add_input = str(input("Please input a string : ")).capitalize()
    print(user_add_input, file=in_file)
    print("<{}> was appended into {} file".format(user_add_input, FILE_PATH))
    in_file.close()


def file_split():
    in_file = open(FILE_PATH, "r")
    total = [song for song in in_file.read().splitlines()]
    print(total)
    for word in total:
        word_splitter = word.split()
        print(word_splitter)


def replace_word():
    in_file = open(FILE_PATH, "r")
    total = [song for song in in_file.read().splitlines()]
    in_file.close()
    print(total)
    nested_list = [word.split() for word in total]
    print(nested_list)
    nested_list[0][-1] = "thing"
    new_list = []
    for line in nested_list:
        new_line = " ".join(line)
        new_list.append(new_line)
    append_file = open(FILE_PATH, "w+")
    for line in new_list:
        print(line, file=append_file)


# replace_word()
# file_split()
# file_append()
# file_write()
# file_read()