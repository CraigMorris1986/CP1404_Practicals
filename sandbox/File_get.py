# This is an example of file retrieval in python.

def file_read():
    in_file = open("text_test", "r") # This 'unpacks' the file/contents into a python variable (object)

    print(in_file.read()) # This will display 'unpacked' file contents through the variable.

    file_content = in_file.read() # This 'saves' the files 'unpacked' read contents into a variable without needing to
    # the .read() function everytime.

    print(type(in_file))

    print(repr(file_content)) # The repr() function prints the files content through the variable in a RAW format (\n etc)

    print(file_content) # This will display 'unpacked' file contents through the saved variable. Doesn't need to
    # unpack again using processor power to use the .read() function again.

    in_file.close() # This closes the file. MUST ALWAYS close the file after its finished its use!

def file_write():
    in_file = open("test_write.txt", "w")
    user_written_input = str(input("Please input a string : ")).capitalize()
    print(user_written_input, file=in_file)
    print("<{}> was entered into {} file".format(user_written_input, in_file))
    in_file.close()

file_write()
# file_read()