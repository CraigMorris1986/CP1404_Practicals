def main(*args):
    """ Type in the age in years as an integer for each person. """
    # keep initialising value outside of for loop
    total = 0
    # use for loop to index through the unknown amount of values
    for i in range(len(args)):
        total = total + args[i]
    mean = total / len(args)
    print(mean)

main(14,17,169,1,2)

# This function shows how to take in an unknown amount of parameters


