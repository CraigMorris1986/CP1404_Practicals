from car import Car
# Unknown error, pycharm highlights error for import statement but when from prac_07.car import Car
# is called python throws an Import Exception, other files using prac_07.car however work as intended.

MENU_OPTIONS = ["d", "r", "q"]


def main():
    car_name = input("Enter your car's name: ").title()
    vehicle = Car(car_name, 100)
    menu(vehicle)
    print("Goodbye {} driver".format(vehicle.name))


def menu(vehicle):
    finished = False
    while not finished:
        print(vehicle)
        print("Menu:\n(D)rive\n(R)efuel\n(Q)uit")
        menu_choice = get_menu_choice()
        if menu_choice == "d":
            drive_distance = get_integer("How many KM do you wish to drive?: ", "distance")
            if vehicle.fuel >= drive_distance:
                print("You have traveled {}KM".format(drive_distance))
            else:
                print("You have traveled {}KM and ran out of fuel".format(vehicle.fuel))
            vehicle.drive(drive_distance)
        elif menu_choice == "r":
            vehicle.add_fuel(refuel_amount)
            refuel_amount = get_integer("How many units of fuel do you want to add to the car?: ", "fuel")
        elif menu_choice == "q":
            finished = True


def get_menu_choice():
    valid = False
    while not valid:
        menu_choice = input("Enter your choice: ").lower()
        if menu_choice in MENU_OPTIONS:
            return menu_choice
        else:
            print("Invalid menu choice")


def get_integer(prompt, unit_type):
    valid = False
    while not valid:
        try:
            number = int(input(prompt))
            if number >= 0:
                return number
            else:
                print("The {} must be >= 0".format(unit_type))
        except ValueError:
            print("Invalid choice")


main()
