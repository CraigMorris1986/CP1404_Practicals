"""This shows how the import function works to import modules into the python code for use. """

# import random >>>... this will import the whole module for use.
# from random import randint >>>... this will import a particular function from the module for use.
# from random import randint as random_integer >>>... this changes the name of a function from the imported module.

import random

print(random.randint(5,20))
print(random.randrange(3,10,2))
print(random.uniform(2.5,5.5))



