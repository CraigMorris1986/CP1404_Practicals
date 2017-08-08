# this is a menu slection test

def main():
    user_name = input("Please enter your name : ").capitalize()
    menu(user_name)
    print("Finished.")
def menu(name):
    quit = False
    while quit == False:
        print("(H)ello\n(G)oodbye\n(Q)uit")
        user_choice = str(input("H / G / Q")).lower()
        if user_choice == "h":
            print(" Hello {}.".format(name))
        elif user_choice == "g":
            print("Goodbye {}.".format(name))
        elif user_choice == "q":
            quit = True
        else:
            print("Invalid choice.")
            user_choice = str(input("H / G / Q")).lower()

main()