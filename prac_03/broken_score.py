"""
A modification of the score.py file that uses a function to return the appropriate value (string) for main() to print.
"""


def score_sorter(user_score):
    """ This function sorts out an integer score value into a print statement. """
    if user_score < 0 or user_score > 100:
        return "Invalid score"
    elif user_score >= 90:
        return "Excellent"
    elif user_score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    score = float(input("Enter score: "))
    assessed_grade = score_sorter(score)
    print(assessed_grade)

main()
