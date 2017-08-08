"""Let’s write a program that gets an integer from the user and does not crash when a non-number is entered.
Copy the code below and modify/add the parts highlighted so that it works and prints the number at the end:
https://github.com/CP1404/Practicals/blob/master/prac_02/exceptions_to_complete.py """

def main():
    finished = False
    result = 0
    while not finished:
        try:
            user_number = int(input("Please enter a number : "))
            finished = True
        except ValueError:
            print(ValueError)
            print("Please enter a valid integer.")
    print("Valid result is {}".format(user_number))


main()