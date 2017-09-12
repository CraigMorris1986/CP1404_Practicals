"""
Intermediate Exercises
Based on the state name example program above, create a program that allows you to look up hexadecimal 
colour code
s like those at 
http://www.color
-
hex.com/color
-
names.html
Use a constant dictionary of about 10 names and write a program that allows a user to enter a name and get 
the code, e.g. entering 
AliceBlue
should show 
#f0f8ff
.
This is a change in the comments
"""


COLOURS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "beige": "#f5f5dc", "black": "#000000", "BlanchedAlmond":
           "#ffebcd", "BlueViolet": "#8a2be2", "brown": "#a52a2a", "burlywood": "#deb887", "CadetBlue": "#5f9ea0",
           "chocolate": "#d2691e"}


def main():
    complete = False
    print("Available colours: ")
    for colour in COLOURS:
        print(colour, end=", ")
    while not complete:
        colour = input("\nType a colour name (capitals matter) : ")
        if colour in COLOURS:
            print("{}s' hexcode is {}".format(colour, COLOURS[colour]))
            complete = True
        else:
            print("invalid colour name")


main()

