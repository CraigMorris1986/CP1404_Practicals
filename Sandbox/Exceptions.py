# This is how to use try and except statements to capture python and user errors for handling.

def main():
    accept = False
    while accept == False:
        try: # the try statement will 'try' and execute the code, if an exception(error) is thrown it stops and skips
             # to the except statement.
            user_age = int(input("Please enter an age : "))
            if user_age < 0:
                print("Age must be a positive number.")
            else:
                accept = True # This loop exit condition will not execute if the user input cannot be made into an INT.

        except ValueError: # This block runs if the try statement fails.
            print("Invalid input.")
            print(ValueError) #You can print the error statement to prevent the code from halting.

    if user_age % 2 == 0:
        print("Yor age is even.")
    else:
        print("Your age is odd.")


main()