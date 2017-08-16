"""
prac_03 file created that displays the contents of files in a folder used for the purpose of commiting and
pushing to Github through pycharm.
"""

import os

print("The files and folders in {} are:".format(os.getcwd()))
items = os.listdir('.')
for item in items:
    print(item)
