from prac_08.guitars_class import Guitar


def main():
    guitars = read_file("guitars.csv")
    guitars = create_guitars(guitars)
    for guitar in guitars:
        print(guitar)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def read_file(file_path):
    file_contents = []
    in_file = open(file_path, "r")
    for line in in_file:
        separated_line = line.split(",")
        file_contents.append(tuple(separated_line))
    in_file.close()
    return file_contents


def create_guitars(guitars):
    guitar_objects = []
    for guitar in guitars:
        item = Guitar(guitar[0], guitar[1], guitar[2])
        guitar_objects.append(item)
    return guitar_objects


main()
