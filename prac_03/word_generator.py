"""
This is a program that takes a user selection of consonants and vowels to randomly generate a string.
"""


import random
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def is_valid_format(user_letter_choice):
    for letter in user_letter_choice:
        if letter != "c" and letter != "v":
            return False
    return True


def main():
    is_user_input_valid = False
    while not is_user_input_valid:
        print("Invalid input.")
        word_format = input("Please use c for a random consonant and v for a random vowel\n"
                            "Example ccvccv : ").lower()
        is_user_input_valid = is_valid_format(word_format)
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    print(word)


main()

