"""
1. Write a program that prompts the user for 5 numbers and then stores each of these in a list called
numbers. The program should then output various interesting things, as in the output below (green
represents user input).
Note that you can use the functions min, max, sum and len, and you can use the append method to
add a number to a list.
Number: 5
Number: 20
Number: 1
Number: 2
Number: 3
The first number is 5
The last number is 3
The smallest number is 1
The largest number is 20
"""


def main():
    numbers = make_numbers_list()
    statement_display(numbers)


def make_numbers_list():
    """This function checks user integer input is greater than zero then constructs a list from those numbers. """
    numbers = []
    finished = False
    while not finished:
        number = get_integer()
        if number < 0:
            finished = True
        else:
            numbers.append(number)
    return numbers


def get_integer():
    """This function checks for a valid integer from user input. """
    valid_number = False
    while not valid_number:
        try:
            number = int(input("Number: "))
            return number
        except ValueError:
            print("Invalid input, please enter a number")


def statement_display(numbers):
    """This function takes in a list of numbers and outputs a statement to screen for the user. """
    print("The first number is {}". format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {:.1f}".format((sum(numbers) / len(numbers))))

main()
