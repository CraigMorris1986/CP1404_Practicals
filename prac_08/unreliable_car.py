from prac_08.car import Car
from random import uniform


class UnreliableCar(Car):
    """Class for a car that has a random chance to fail instead of driving."""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = float(reliability)  # sets vehicles reliability as a percentage

    def drive(self, distance):
        """Checks reliability against a RNG to see if the drive method will be executed."""
        distance_drove = 0
        if self.reliability >= uniform(0, 100):
            distance_drove = super().drive(distance)
        return distance_drove


def unreliable_car_test():
    the_bomb = UnreliableCar("The Bomb", 100, 50.5)
    for _ in range(10):
        the_bomb.drive(10)
        print(the_bomb)


if __name__ == "__main__":
    unreliable_car_test()
