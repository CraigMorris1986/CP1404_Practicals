from prac_08.car import Car
from prac_08.taxi import Taxi


def main():
    prius = Taxi("Prius 1", 100)
    print(prius)
    prius.drive(40)
    print(prius, "\n", prius.current_fare_distance)
    prius.start_fare()
    prius.drive(100)
    print(prius, "\n", prius.current_fare_distance)


main()
