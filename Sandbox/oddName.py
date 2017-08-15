"""
Add a Python file called oddName.py and enter just a single docstring (triple-quoted comment) at the
top with your name in it. Craig Morris
"""

def main():
    user_name = ""
    while len(user_name) == 0:
        user_name = input("Please enter name : ")
    for index in range(0, len(user_name), 2):
        print(user_name[index], end=" ")

main()