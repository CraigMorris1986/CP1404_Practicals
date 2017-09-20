from prac_07.car import Car

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
            drive_car(vehicle)
        elif menu_choice == "r":
            add_fuel(vehicle)
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


def drive_car(vehicle):
    drive_distance = get_integer("How many KM do you wish to drive?: ", "distance")
    if vehicle.fuel > drive_distance:
        vehicle.fuel -= drive_distance
        vehicle.odometer += drive_distance
        print("{} drove {}KM\n".format(vehicle.name, drive_distance))
    else:
        vehicle.odometer += vehicle.fuel
        print("{} drove {}KM and ran ot of fuel\n".format(vehicle.name, vehicle.fuel))
        vehicle.fuel -= vehicle.fuel


def add_fuel(vehicle):
    refuel_amount = get_integer("How many units of fuel do you want to add to the car?: ", "fuel")
    vehicle.fuel += refuel_amount


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
