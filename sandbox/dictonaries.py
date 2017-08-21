""" Dictionaries -
dictionaries are collections but they are not sequences such as lists, strings or tuples
there is no order to the elements of a dictionary
in fact, the order (for example, when printed) might change as elements are added or deleted. 

Access requires [], but the key is the index!

my_dict.clear() – empty the dictionary
my_dict.update(other_dict) – for each key in other_dict, update my_dict with that key/value pair
my_dict.copy() – shallow copy
my_dict.pop(key)– remove key, return value
my_dict.items() – all the key/value pairs as tuples
my_dict.keys() – all the keys
my_dict.values() – all the values
my_dict.get() method returns the value associated with a dict key or a default value provided as second argument.

zip creates a list of pairs (tuples) from two parallel lists
zip("abc", [1, 2, 3]) yields
[('a',1), ('b',2), ('c',3)]
That's good for building dictionaries. We call the dict function which takes a list of pairs to make a dictionary
dict(zip("abc", [1,2,3])) yields
{'a': 1, 'c': 3, 'b': 2}

"""

names_and_ages = {"Craig": 31, "Bam": 30, "Hannah": 25}  # sets a dictionary type by use of {} - KEY: VALUE
print(names_and_ages)

names_and_ages["Jaiden"] = 6  # This adds a new pair to the dictionary.
print(names_and_ages)
print(names_and_ages["Hannah"])  # this will print the value of the KEY that was called dict[KEY] = VALUE of [KEY]

# Existing keys in a dictionary can be reassigned a new value
names_and_ages["Craig"] = 19
print(names_and_ages)

print(len(names_and_ages))  # The len() function works on dictionaries

boolean = "Bam" in names_and_ages  # element can be check if in the dictionary
print(boolean)

for name in names_and_ages:  # The keys can be indexed through the dictionary
    print(name)

for name, age in names_and_ages.items():  # the .items() method is needed to unpack both keys and values to iterate.
    print(name, age)

new_dict = {}  # .get() can be used to count each time a key is used in a dict and create a new dict with the count.
for name in names_and_ages:
    new_dict[name] = new_dict.get(name, 0) + 1
print(new_dict)

print(max(names_and_ages))  # This will only look through the KEYS in the dict.
