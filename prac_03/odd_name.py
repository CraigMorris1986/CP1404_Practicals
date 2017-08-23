"""
Add a Python file called oddName.py and enter just a single docstring (triple-quoted comment) at the
top with your name in it. Craig Morris
"""


def main():
    user_name = get_name()
    print_second_letter(user_name)


def print_second_letter(user_name, letter_index=2):  # gave the letter index a default value of 2
    for index in range(0, len(user_name), letter_index):
        print(user_name[index], end=" ")


def get_name():
    user_name = input("Please enter name : ")
    while len(user_name) == 0:
        print("Unfortunately your name can not be left blank.")
        user_name = input("Please enter name : ")
    return user_name


main()
