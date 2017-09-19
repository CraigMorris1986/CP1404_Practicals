from prac_07.guitar import Guitar


def main():
    print("My guitars!")
    guitars = add_guitar()
    for index, guitar in enumerate(guitars):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(Vintage)"
        print("Guitar {}: {:>20} ({}), cost ${:>10,.2f} {}".format(index + 1, guitar.name, guitar.year, guitar.price,
                                                                   vintage_string))


def add_guitar():
    guitars = []
    complete = False
    while not complete:
        name = str(input("Name: "))
        if len(name) == 0:
            return guitars
        manufacture_year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, manufacture_year, cost)
        guitars.append(guitar)
        print("{} ({}) : ${:.2f} added".format(guitar.name, guitar.year, guitar.price))


main()
