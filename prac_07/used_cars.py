from prac_07.car import Car


def main():
    my_car = Car("Jeep", 180)
    my_car.drive(30)
    print("fuel = {}".format(my_car.fuel))
    print("Odometer = {}".format(my_car.odometer))
    print(my_car)

    my_limo = Car("Limo", 100)
    my_limo.add_fuel(20)
    print(my_limo.fuel)
    my_limo.drive(115)
    print(my_limo.odometer)
    print(my_limo)

main()
