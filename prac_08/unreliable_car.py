from prac_08.car import Car
from random import random


class UnreliableCar(Car):
    def __init__(self, name, fuel):
        super().__init__(name, fuel)
        self.reliability = 0.5  # sets vehicles reliability as a percentage

    def drive(self, distance):
        if self.reliability >= random():
            distance_drove = super().drive(distance)
            print("{} started today and drove {}KM".format(self.name, distance_drove))
        else:
            self.fuel -= 1
            print("{} sputters and fails to start using 1 unit of fuel".format(self.name))


def unreliable_car_test():
    the_bomb = UnreliableCar("The Bomb", 100)
    print(the_bomb)
    the_bomb.drive(50)
    print(the_bomb)


if __name__ == "__main__":
    unreliable_car_test()
