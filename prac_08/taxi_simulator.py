from prac_08.taxi import Taxi
from prac_08.sivler_service_taxi import SilverServiceTaxi

TAXIS = [Taxi("Yellow Cab", 100), SilverServiceTaxi("Limo", 120, 2), SilverServiceTaxi("Stretch Humvee", 200, 4)]
OPTIONS = ["c", "d", "q"]


def main():
    print("Let's go for a taxi drive!")
    menu()
    print("Will that be cash or EFTPoS?")


def menu():
    """Houses the menu loop for the program, allowing the user to choose a taxi, drive, and quit."""
    is_finished = False
    total_fare = 0
    current_taxi = None
    while not is_finished:
        print("(C)hoose taxi\n(D)ive\n(Q)uit")
        user_choice = get_choice()
        if user_choice == "c":
            current_taxi = select_taxi()
        elif user_choice == "d":
            total_fare = ride_taxi(current_taxi, total_fare)
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
        elif user_choice == "q":
            is_finished = True
        print("Bill to date: ${:.2f}".format(total_fare))


def ride_taxi(taxi, fare):
    """Drives the taxi that is currently selected, if no taxi is selected will return an error statement to user."""
    if taxi is None:
        print("You must get in a taxi first!")
    else:
        distance = get_integer("How far would you like to go?")
        taxi.drive(distance)
        fare += taxi.get_fare()
        return fare


def select_taxi():
    """Displays the Taxi instances in the TAXI array and returns the users taxi selection."""
    print("Available Taxis")
    for index, taxi in enumerate(TAXIS):
        print("{} - {}".format(index, taxi))
    taxi_choice = get_integer("Choose taxi: ")
    while taxi_choice not in range(len(TAXIS)):
        print("Please select a taxi from the list")
        taxi_choice = get_integer("Choose taxi: ")
    return TAXIS[taxi_choice]


def get_choice():
    """Gets user choice for menu selections and will error check user input."""
    choice = input(">>> ").lower()
    while choice not in OPTIONS:
        print("Invalid choice")
        choice = input(">>> ").lower()
    return choice


def get_integer(prompt):
    """Gets a user integer value and returns it for use in the program. Will error check for a valid integer. """
    number = None
    while number != type(int):
        try:
            number = int(input(prompt))
            while number < 0:
                print("number must be > than 0")
                number = int(input(prompt))
            return number
        except ValueError:
            print("Please enter a number")


main()
