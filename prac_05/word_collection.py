"""
Do-from-scratch Exercise
Write a program to count the occurrences of words in a string. The program should ask the user for a string, 
then print the counts of how many of each word are in the file.
The output should look like this:
Text: 
this is a collection of words of nice words this is a fun thing it is
a : 2
collection : 1
fun : 1
is : 3
it : 1
nice : 1
of : 2
thing : 1
this : 2
words : 2
"""


def main():
    word_collection = {}
    user_string = str(input("Please type some text: "))
    words = user_string.split()
    for word in words:
        if word in word_collection:
            word_collection[str(word).lower()] += 1
        else:
            word_collection[str(word).lower()] = 1
    length_of_longest_word = find_longest_word(words)
    for word, count in sorted(word_collection.items()):
        print("{:<{}} = {}".format(word, length_of_longest_word, count))


def find_longest_word(words):
    length = 0
    for word in words:
        if len(word) > length:
            length = len(word)
    return length

main()
