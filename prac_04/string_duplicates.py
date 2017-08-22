"""
Write a program that asks the user for an indefinite set of strings - until an empty string is entered - then
prints all of the strings that were repeated.
E.g. if the user entered: “hello”, “world is good”, “hello”, “john”, “good”… the program would print
“Strings repeated: hello”.
If no repeated strings are entered, the program should print “No repeated strings entered”.
"""


def main():
    strings = get_string()
    # print(strings)
    sorted_strings = sorted(strings)
    # print(sorted_strings)
    number_of_duplicates = 0
    for index in range(len(strings)):
        try:
            if sorted_strings[index] == sorted_strings[index + 1]:
                print("Strings repeated: {}".format(sorted_strings[index]))
                number_of_duplicates += 1
        except IndexError:
            pass
    if number_of_duplicates == 0:
        print("No repeated strings entered")


def get_string():
    strings = []
    finished = False
    while not finished:
        string = str(input("Enter a string: "))
        if len(string) == 0:
            finished = True
        else:
            strings.append(string)
    return strings


main()
