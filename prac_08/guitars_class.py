class Guitar:
    """Creates a Guitar object"""

    def __init__(self, name, year, price):
        self.name = str(name)
        self.year = int(year)
        self.price = float(price)

    def __str__(self):
        string_format = "{} manufactured in {} - Price ${:.2f}".format(self.name, self.year, self.price)
        return string_format

    def __lt__(self, other):
        return self.year < other.year


def class_testing():
    pass


if __name__ == "__main__":
    class_testing()
