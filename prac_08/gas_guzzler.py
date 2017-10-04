from prac_08.car import Car
from random import random


class GasGuzzler(Car):
    """A Car subclass that uses more fuel to travel per km."""

    def __init__(self, name, fuel):
        super().__init__(name, fuel)
        self.fuel_consumption_per_km = round(1 + random(), 2)

    def __str__(self):
        return "{}, fuel consumption per km {}".format(super().__str__(), self.fuel_consumption_per_km)

    def drive(self, distance):
        if distance > self.fuel * self.fuel_consumption_per_km:
            distance = self.fuel * self.fuel_consumption_per_km
            self.fuel = 0
        else:
            self.fuel -= distance * self.fuel_consumption_per_km
        self.odometer += distance
        return distance


def test_function():
    car = GasGuzzler("Rusty", 100)
    print(car)
    car.drive(50)
    print(car)
    car.drive(50)
    print(car)


if __name__ == "__main__":
    test_function()
