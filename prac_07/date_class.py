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
        if self.day < 10:
            string_format = "0{}/{:>2}/{:>4}".format(self.day, self.month, self.year)
        elif self.month < 10:
            string_format = "{:>2}/0{}/{:>4}".format(self.day, self.month, self.year)
        elif self.day and self.month < 10:
            string_format = "0{}/0{}/{:>4}".format(self.day, self.month, self.year)
        else:
            string_format = "{:>2}/{:>2}/{:>4}".format(self.day, self.month, self.year)
        return string_format

    def add_days(self, number_of_days):
        self.day += number_of_days
        while self.day > DAYS_IN_MONTHS[self.month]:
            day_overflow = self.day - DAYS_IN_MONTHS[self.month]
            self.day = day_overflow
            self.month += 1
            while self.month > len(DAYS_IN_MONTHS):
                self.month -= len(DAYS_IN_MONTHS)
                self.year += 1


def test():
    today = Date(2017, 2, 28)
    print(today)
    today.add_days(123)
    print(today)
    today.add_days(365)
    print(today)


if __name__ == "__main__":
    test()
