"""This checks a string for all the vowels it contains and outputs to screen. """

VOWELS = ["a", "e", "i", "o", "u"]  # Give lists a plural name as they contain more than one piece of data.


def main():
    user_name = str(input("Please enter your name : "))
    user_name_letter_count = len(user_name) - user_name.count(" ")
    vowel_count = 0
    for letter in user_name.lower():
        if letter in VOWELS:
            vowel_count += 1
    print("Out of {} letters, {} has {} vowels".format(user_name_letter_count, user_name, vowel_count))


main()
