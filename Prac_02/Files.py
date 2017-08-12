"""Do all of the following in a single file called files.py:
1. Write a program that asks the user for their name, then opens a file called “name.txt” and writes that
name to it.
2. Write a program that opens “name.txt” and reads the name (as above) then prints,
“Your name is Bob” (or whatever the name is in the file).
3. Create a text file called “numbers.txt” (You can create a simple text file in PyCharm with Ctrl+N, choose
“File” and save it in your project). Put the numbers 17 and 42 on separate lines in the file and save it:
17
42
Write a program that opens “numbers.txt”, reads the numbers and adds them together then prints the
result, which should be… 59.
4. Extended (perhaps only do this if you’re cruising… if you are struggling, just read the solution) …
Now extend your program so that it can print the total for a file containing any number of numbers. """

OUTPUT_FILE_NAME = "name.txt"
OUTPUT_FILE_NUMBERS = "numbers.txt"


def name_reader():
    in_file_name = open(OUTPUT_FILE_NAME, "w")
    user_name = input(" Please enter your name : ").capitalize()
    print(user_name, file=in_file_name)
    in_file_name = open(OUTPUT_FILE_NAME, "r")
    user_name = in_file_name.read()
    print("Your name is {}".format(user_name))
    in_file_name.close()


def number_reader():
    read_file_numbers = open(OUTPUT_FILE_NUMBERS, "r")
    number_list = read_file_numbers.readlines()
    number_total = 0
    for number in range(len(number_list)):
        number_total += int(number_list[number])
    print(number_total)
    read_file_numbers.close()


number_reader()
name_reader()
