"""
GPS (Gopher Population Simulator)
A secret population of 1000 gophers lives near the library. Every year, a random number of gophers is
born, between 10% of the current population, and 20%. (e.g. 15% of the gophers might give birth,
increasing the population by 150). Also each year, a random number of gophers die, between 5% and
25% (e.g. 8% of the gophers might die, reducing the population by 80).
"""

from random import randrange
from time import sleep


def main():
    gopher_population = 1000
    print("Welcome to Gopher Population Simulator!\nStarting population {}".format(gopher_population))
    amount_of_years = valid_years()
    for year in range(amount_of_years):
        print("YEAR {}\n***************".format(year + 1))
        gopher_population = gopher_population_modifier(gopher_population)
        sleep(1)
        if gopher_population <= 0:
            print("All the gophers have died :(")
            break
    print("Thanks for watching the gophers :)")


def gopher_population_modifier(current_population):
    births = int(current_population * (randrange(10, 21) / 100))
    deaths = int(current_population * (randrange(5, 26) / 100))
    new_population = current_population + births - deaths
    print("{} gophers were born :) {} gophers died :(\nTotal gopher population : {}\n".format
          (births, deaths, new_population))
    return new_population


def valid_years():
    years_spent_watching = 0
    while years_spent_watching <= 0 or years_spent_watching > 60:
        try:
            years_spent_watching = int(input("How many years do you want to watch the gophers for? : "))
            if years_spent_watching > 60:
                print("Please enter less than 60 years, you don't want to waste your life watching gophers do you?")
            elif years_spent_watching <= 0:
                print("Please enter a number larger than 0 so you can actually watch the gophers.")
        except ValueError:
            print(ValueError)
            print("Invalid input, please enter a number of years.")
    return years_spent_watching


main()
