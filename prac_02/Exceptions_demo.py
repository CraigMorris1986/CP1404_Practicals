"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?

    When an object type cannot be acted upon in a certain fashion, such as converting an english letter to an integer or
    float.

2. When will a ZeroDivisionError occur?

    When attempting to divide an integer or float by the number zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?

    Yes, by placing the denominator selection in a while loop checking the see if the integer is greater than zero.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator <= 0:
        denominator = int(input("Enter the denominator larger than 0: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")