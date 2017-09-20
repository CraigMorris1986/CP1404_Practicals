from prac_07.guitar import Guitar


def main():
    instrument = Guitar("Stringy", 1950, 1225)
    print("expected Stringy... got {}".format(instrument.name))
    print("expected 67... got {}".format(instrument.get_age()))
    print("expected True... got {}".format(instrument.is_vintage()))


main()
