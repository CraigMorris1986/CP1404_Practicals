"""
“Quick Pick” Lottery Ticket Generator
Write a program that asks the user how many “quick picks” they wish to generate. The program then
generates that many lines of output. Each line consists of six random numbers between 1 and 45.
Each line should not contain any repeated number. Each line of numbers should be displayed in
ascending order.

Note: Python's random function has a sample method, which returns a selection from a list. This is a
nice way to solve this problem... but it's too easy :) Do not use it for this program.
Your code should produce output that matches this sample output (except the numbers are random):

How many quick picks? 5
9 10 11 32 38 44
2 9 12 14 28 30
5 10 16 22 35 42
1 2 16 22 37 40
1 17 20 23 25 27
"""

from random import randint

AMOUNT_OF_NUMBERS = 6
STARTING_NUMBER = 1
ENDING_NUMBER = 46


def main():
    number = integer_getter("How many quick picks? ")
    for index in range(number):
        quick_pick = generator()
        print("{} {} {} {} {} {}".format(quick_pick[0], quick_pick[1], quick_pick[2], quick_pick[3], quick_pick[4]
                                         , quick_pick[5]))


def integer_getter(print_statement):
    """This function checks for a valid integer from user input. """
    valid_number = False
    while not valid_number:
        try:
            number = int(input(print_statement))
            valid_number = True
        except ValueError:
            print("Invalid input, please enter a number")
    return number


def generator():
    random_numbers = []
    while len(random_numbers) != AMOUNT_OF_NUMBERS:
        random_number = randint(STARTING_NUMBER, ENDING_NUMBER)
        if random_number not in random_numbers:
            random_numbers.append(random_number)
    quick_pick = sorted(random_numbers)
    return quick_pick


main()
