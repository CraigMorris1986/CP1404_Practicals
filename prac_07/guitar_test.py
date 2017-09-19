from prac_07.guitar import Guitar


def main():
    instrument = Guitar("Stringy", 1950, 1225)
    print(instrument)
    print(instrument.get_age())
    print(instrument.is_vintage())


main()
