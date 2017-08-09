def score_sorter():
    """ This function sorts out an integer score value into a print statement. """
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print ("Invalid score")
    elif score >= 90:
        print ("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

score_sorter()
