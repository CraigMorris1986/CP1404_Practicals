"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []  # Initialises and empty list to hold each months income.
    number_of_months = integer_getter("How many months? ")  # Function to check for user input errors.

    for month in range(1, number_of_months + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        incomes.append(income)

    report_printer(incomes, number_of_months)


def report_printer(incomes, number_of_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


def integer_getter(print_statement):
    """This function checks for a valid integer from user input. """
    valid_number = False
    number = 0
    while not valid_number:
        try:
            number = int(input(print_statement))
        except ValueError:
            print("Invalid input")
        if number <= 0:
            print("Number must be greater than zero")
        else:
            valid_number = True
    return number


main()
