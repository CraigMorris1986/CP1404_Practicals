"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# 2DO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(STATE_NAMES)


def main():
    state = input("Enter short state: ").upper()
    complete = False
    while not complete:
        if state in STATE_NAMES:
            print(state, "is", STATE_NAMES[state], "\n")
            complete = True
        else:
            print("Invalid short state")
            state = input("Enter short state: ").upper()

    for abbreviation, state_name in sorted(STATE_NAMES.items()):
        print("{:<3} is {:<28}".format(abbreviation, state_name))


main()
