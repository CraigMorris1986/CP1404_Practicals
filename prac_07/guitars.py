from prac_07.guitar import Guitar


def main():
    print("My guitars!")
    guitars = get_guitars()
    for index, guitar in enumerate(guitars):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(Vintage)"
        print("Guitar {}: {:>20} ({}), cost ${:>10,.2f} {}".format(index + 1, guitar.name, guitar.year, guitar.price,
                                                                   vintage_string))


def get_guitars():
    guitars = []
    name = str(input("Name: "))
    while name != "":
        manufacture_year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, manufacture_year, cost)
        guitars.append(guitar)
        print("{} ({}) : ${:.2f} added".format(guitar.name, guitar.year, guitar.price))
        name = str(input("Name: "))
    return guitars


main()
