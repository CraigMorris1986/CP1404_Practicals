# import datetime
#
#
# class Date(datetime):  # Finished!
#     pass

DAYS_IN_MONTHS = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


class Date:
    """A date class"""

    def __init__(self, year, month, day):
        if month not in DAYS_IN_MONTHS:
            print("invalid")
        elif day > DAYS_IN_MONTHS[month]:
            print("too many days")
        else:
            self.year = year
            self.month = month
            self.day = day

    def __str__(self):
        string_format = "{}/{}/{}".format(self.day, self.month, self.year)
        return string_format


def test():
    today = Date(2017, 2, 31)
    print(today)
    print(DAYS_IN_MONTHS)

test()
