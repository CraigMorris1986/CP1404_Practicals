# This is the general layout for functions in python.

def main(): # Always start with the 'main()' function, this houses the entire program in a readable format.

    celsius_temp = int(input(" Please enter temp in Celsius : "))

    print("{} degrees kelvin".format(celsius_to_kelvin(celsius_temp)))

def celsius_to_kelvin(celsius): # takes a parameter as 'celsius' and makes it a local variable.
    kelvin = celsius + 273.15 # performs a task or calculation.
    return kelvin # return statement passes back a value to the previous function level.


main()