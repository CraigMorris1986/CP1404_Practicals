"""
Convert parallel lists into a dictionary...
Recall that it’s possible to represent information in the form of parallel lists where the indices determine 
how the information is related across lists. For example:
names = ["Jack", "Jill", "Harry"]
dobs =  [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]
This means Jack was born on 12/4/1999, Jill was born on 1/1/2000, and Harry was born on 27/3/1982. 
Write a program using a dictionary instead of the above parallel lists that allows the user to enter the 
date-of-birth details for 5 people, and have it display their individual ages.
Hint: you can split() a string like “12/4/1999”, as we did in the lecture last week.
"""


def main():
    birthdays = {}
    for _ in range(5):
        name = str(input("Name: ")).title()
        day_date = get_date(1, 31)
        month_date = get_date(1, 12)
        year = get_date(1900, 2017)
        birthdays[name] = (day_date, month_date, year)
    for name, dates in birthdays.items():
        print("{}s birthday is on {}/{}/{}".format(name, dates[0], dates[1], dates[2]))


def get_date(lower_limit, upper_limit):
    valid = False
    while not valid:
        try:
            date = int(input("Enter a date : "))
            if date < lower_limit or date > upper_limit:
                print("Invalid date range")
            else:
                valid = True
        except ValueError:
            print("Invalid input")
    return date



main()
