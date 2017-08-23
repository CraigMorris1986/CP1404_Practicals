"""
Warm-Up

numbers = [3, 1, 4, 1, 5, 9, 2]

First, write down your answers to these questions without running the code, then use Python to see if you were
correct. What values do the following expressions have?

numbers[0] == 3
numbers[-1] == 2
numbers[3] == 1
numbers[:-1] == [3, 1, 4, 1, 5, 9] slices up to but not including the last index
numbers[3:4] == [1]
5 in numbers == True
7 in numbers == False
"3" in numbers == False , list is instinctively read as int by python
numbers + [6, 5, 3] == nothing, missing the .append() method to add to list

Write Python expressions (in the IDE) to achieve the following:
1. Change the first element of numbers to “ten”
2. Change the last element of numbers to 1
3. Get all the elements from numbers except the first two
4. Check if 9 is an element of numbers
"""


numbers = [3, 1, 4, 1, 5, 9, 2]

numbers[0] = "ten"
numbers[-1] = 1
numbers_sliced = numbers[2:]
print(9 in numbers)
