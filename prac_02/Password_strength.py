def password(pass_attempt):
    user_attempt = []
    if len(pass_attempt) < 7:
        print("Invalid password, it must be a minimum of 7 characters long")
        return False
    for i in range(len(pass_attempt)):
        user_attempt.append(pass_attempt[i])
    special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '`', '~', '-', '_', '=', '+', '/', '[', ']', '{', '}',
               ';', ':', '<', '>', '?', "'", ]
    check_1 = False
    check_2 = False
    check_3 = False
    check_4 = False
    while check_1 == False and check_2 == False and check_3 == False and check_4 == False:
        for char in user_attempt:
            if char.isupper():
                check_1 = True
            elif char.isdigit():
                check_2 = True
            elif char.islower():
                check_3 = True
            elif char in special:
                check_4 = True
    if check_1 == True and check_2 == True and check_3 == True and check_4 == True:
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
