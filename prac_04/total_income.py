"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []  # Initialises and empty list to hold each months income.
    number_of_months = get_integer("How many months? ")  # Function to check for user input errors.

    for month in range(1, number_of_months + 1):
        valid_income = False
        while not valid_income:
            try:
                income = float(input("Enter income for month {}: ".format(month)))
                valid_income = True
            except ValueError:
                print("Invalid input, please enter a number")
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, len(incomes) + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


def get_integer(prompt):
    """This function checks for a valid integer from user input. """
    valid_number = False
    while not valid_number:
        try:
            number = int(input(prompt))
            if number <= 0:
                print("Number must be greater than zero")
            else:
                valid_number = True
        except ValueError:
            print("Invalid input")
    return number


main()
