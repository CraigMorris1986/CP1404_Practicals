"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit_input = valid_temperature_input()
            celsius_temperature = convert_to_celsius(fahrenheit_input)
            print("Result: {:.2f} C".format(celsius_temperature))
        elif choice == "F":
            celsius_input = valid_temperature_input()
            fahrenheit_temperature = convert_to_fahrenheit(celsius_input)
            print("Result: {:.2f} F".format(fahrenheit_temperature))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def valid_temperature_input():
    is_valid = False
    while not is_valid:
        try:
            temperature = float(input("Please enter the temperature : "))
            is_valid = True
        except ValueError:
            print(ValueError)
            print("Invalid input.")
    return temperature


main()
