"""This is a class that creates guitar objects."""
VINTAGE_THRESHOLD = 50
CURRENT_YEAR = 2017


class Guitar:
    def __init__(self, name="", year=0, price=0):
        self.name = name
        self.year = year
        self.price = price

    def __str__(self):
        string_format = "{} ({}) : ${:.2f}".format(self.name, self.year, self.price)
        return string_format

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        if CURRENT_YEAR - self.year > VINTAGE_THRESHOLD:
            return True
        else:
            return False
