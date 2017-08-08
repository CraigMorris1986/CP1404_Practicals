def password(pass_attempt):
    user_attempt = []
    if len(pass_attempt) < 7:
        print("Invalid password, it must be a minimum of 7 characters long")
        return False
    for i in range(len(pass_attempt)):
        user_attempt.append(pass_attempt[i])
    # got lazy and just made a list of characters
    special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '`', '~', '-', '_', '=', '+', '/', '[', ']', '{', '}',
               ';', ':', '<', '>', '?', "'", ]
    check1 = False
    check2 = False
    check3 = False
    check4 = False
    while check1 == False and check2 == False and check3 == False and check4 == False:
        for char in user_attempt:
            if char.isupper():
                check1 = True
            elif char.isdigit():
                check2 = True
            elif char.islower():
                check3 = True
            elif char in special:
                check4 = True
    if check1 == True and check2 == True and check3 == True and check4 == True:
        return True
    else:
        print("you must have an Uppercase letter, a number, a lower case letter, and a Special Character")
        return False


def main():
    accepted = False
    while not accepted:
        attempt = input("Please enter a password : ")
        accepted = password(attempt)
    print("Password accepted, have a nice day :)")

main()