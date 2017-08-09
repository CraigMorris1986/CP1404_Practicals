"""
This program displays the ascii conversions for characters and the reverse from number to character.
"""


def ascii_code_converter():
    user_input = str(input("Please enter a character : "))
    while len(user_input) != 1:
        print("Field cannot be blank or have more than one character.")
        user_input = input("Please enter a character : ")
    print("The ASCII code for {} is {}".format(user_input, ord(user_input)))


def number_to_character():
    valid_user_input = number_range_check()
    while valid_user_input < 33 or valid_user_input > 127:
        print("Number selected is outside of range..")
        valid_user_input = number_range_check()
    print("The character for {} is {}".format(valid_user_input, chr(valid_user_input)))


def number_range_check():
    valid_input = False
    while not valid_input:
        try:
            user_choice = int(input("Enter a number between 33 and 127 : "))
            valid_input = True
        # except TypeError:
        #     print(TypeError)
        #     print("Please enter a number")
        except ValueError:
            print(ValueError)
            print("Please enter a number")
    return user_choice


def main():
    ascii_code_converter()
    number_to_character()


main()
# ascii_code_converter()
# number_to_character()
# number_range_check()
