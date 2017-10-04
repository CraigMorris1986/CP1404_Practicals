from prac_08.guitars_class import Guitar


def main():
    guitars = get_guitar()
    for guitar in guitars:
        print(guitar)
    save_guitars("my_guitars.csv", guitars)


def get_guitar():
    finished = False
    guitars = []
    while not finished:
        guitar_name = input("Name: ").title()
        if not guitar_name:
            break  # Exits the loop if a blank guitar name is entered.
        guitar_year = int(get_number("Year: "))
        guitar_price = get_number("Price: ")
        guitar = Guitar(guitar_name, guitar_year, guitar_price)
        guitars.append(guitar)
    return guitars


def get_number(prompt):
    number = None
    while not number:
        try:
            number = float(input(prompt))
        except ValueError:
            print("Input must be a number")
    return number


def save_guitars(file_path, guitars):
    out_file = open(file_path, "w")
    for guitar in guitars:
        guitar_details = [guitar.name, str(guitar.year), str(guitar.price)]
        file_line = ",".join(guitar_details)
        print(file_line, file=out_file)
    out_file.close()


main()
