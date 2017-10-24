"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_07.car import Car


def repeat_string(string, number):
    """Repeat string s, n times, with spaces in between."""
    repeated_string = []
    for _ in range(number):
        repeated_string.append(string)
    repeated_string = " ".join(repeated_string)
    return repeated_string


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # TODO: 1. fix the repeat_string function above so that it passes the test
    # Hint: "-".join(["yo", "yo"] -> "yo-yo"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # TODO: 2. write assert statements to show if Car sets the fuel correctly
    assert test_car.fuel == 0, "Car default fuel != 0"
    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    test_car = Car(fuel=10)
    assert test_car.fuel == int(10), "Car fuel attribute is not an int type"


run_tests()

# TODO: 3. Uncomment the following line and run the doctests
doctest.testmod()


# TODO: 4. Fix the failing is_long_word function
# (don't change the tests, but the function!)

# TODO: 5. Write and test a function to format a phrase as a sentence,
# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests so that:
# 'hello' -> ''Hello.'
# 'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more you decide (that's valid!)
# then write the body of the function so that the tests pass

def sentence_constructor(sentence):
    """Constructs a sentence into more grammatical correct sentence phrase
    >>> print(sentence_constructor("this is a sentence")) 
    This is a sentence.
    
    >>> print(sentence_constructor("Monty Python"))
    Monty Python.
    
    >>> print(sentence_constructor("A     proper     sentence."))
    A proper sentence.
    
    >>> print(sentence_constructor("word documents are saved as .docx")) 
    Word documents are saved as .docx.
    """
    words = str(sentence).split(" ")
    while "" in words:  # Removes all blank entries created in array due to extra spaces in sentence.
        for word in words:
            if word == "":
                words.remove(word)
    words[0] = words[0].title()
    if words[-1][-1] == ".":  # checks the last character of the last word if it's already a period.
        pass
    else:
        words[-1] = words[-1] + "."
    return " ".join(words)


doctest.testmod()
