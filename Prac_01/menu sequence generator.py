# This is a sequence generator with a menu.


def main():
    starting_number = int(input("Please enter a starting number : "))
    ending_number = int(input("please enter an ending number : "))

    while ending_number - starting_number > 10000:
        print("Numbers are too far apart and will generate a large report\n"
              "Please enter two numbers within 10,000 of each other")
        starting_number = int(input("Please enter a starting number : "))
        ending_number = int(input("please enter an ending number : "))

    exit_game = False
    while exit_game != True:
        user_choice = input("(E)ven numbers\n(O)dd numbers\n(S)quare\n(Q)uit : ").lower()
        if user_choice == "q":
            exit_game = True
        elif user_choice == "e":
            even_sequence(starting_number, ending_number)
        elif user_choice == "o":
            odd_sequence(starting_number, ending_number)
        elif user_choice == "s":
            square_sequence(starting_number, ending_number)

    print("Farewell.")

def even_sequence(start_point, end_point):
    if start_point % 2 != 0:
        start_point += 1
    for number in range(start_point, end_point + 1, 2):
        print(number, end=" ")
    print("\n")

def odd_sequence(start_point, end_point):
    if start_point % 2 == 0:
        start_point += 1
    for number in range(start_point, end_point + 1, 2):
        print(number, end=" ")
    print("\n")

def square_sequence(start_point, end_point):
    for number in range(start_point, end_point + 1):
        print((number + start_point) **2, end=" ")
    print("\n")

main()