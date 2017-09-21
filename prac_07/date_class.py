DAYS_IN_MONTHS = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


class Date:
    """A date class"""

    def __init__(self, year, month, day):
        self.year = year
        if month not in DAYS_IN_MONTHS:
            raise ValueError("Month must be an integer or is out of range 1-12")
        self.month = month
        if day > DAYS_IN_MONTHS[self.month]:
            raise ValueError("Too many days in month")
        self.day = day

    def __str__(self):
        string_format = "{}/{}/{}".format(self.day, self.month, self.year)
        return string_format

    def add_days(self, number_of_days):
        if self.day + number_of_days > DAYS_IN_MONTHS[self.month]:
            raise IndexError("Too many days")
        self.day += number_of_days


def test():
    today = Date(2017, 2, 30)
    print(today)
    print(DAYS_IN_MONTHS)
    today.add_days(1)
    print(today)


if __name__ == "__main__":
    test()
