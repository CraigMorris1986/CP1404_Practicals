from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A subclass of Taxi allowing for a fare multiplier attribute and a one off flagfall fee attribute."""
    flagfall = 4.50  # class variables are shared throughout all instances of this class

    def __init__(self, name, fuel, fanciness_scale):
        super().__init__(name, fuel)
        self.fanciness = float(fanciness_scale)
        self.price_per_km *= self.fanciness

    def __str__(self):
        """ Returns a string like Taxi with the flagfall attribute added to the end."""
        return "{} plus flagfall of {:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Calculates the fare cost like Taxi and adds the one off flagfall fee."""
        return super().get_fare() + self.flagfall
