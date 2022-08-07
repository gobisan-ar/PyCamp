# Merge two dictionaries into one

dict_1 = {'John': 15, 'Rick': 10, 'Misa': 12}
dict_2 = {'Bonnie': 18, 'Rick': 20, 'Matt': 16}

# update method
dict_1.update(dict_2)
print(dict_1)
print()

dict_1 = {'John': 15, 'Rick': 10, 'Misa': 12}
dict_2 = {'Bonnie': 18, 'Rick': 20, 'Matt': 16}

# unpack operator
dict_3 = {**dict_1, **dict_2}
print(dict_3)
print()

d = {0: 0, 1: 1, 2: 2, 3: 3}

# d[4] = d.pop(0)
x = d.pop(0)
d[4] = x

print(d)
print()

# Delete set of keys from Python Dictionary

my_dict = {"Fruit": "Apple",
           "Vegetable": "Carrot",
           "Pet": "Dog",
           "Book": "Essentialism",
           "Grain": "Barley"}

keysToRemove = ["Pet", "Book"]

for key in keysToRemove:
    my_dict.pop(key)

print(my_dict)
print()

# Create a new dictionary by extracting set of keys from a given dictionary
sub_dict = {'math': 100, 'chem': 98, 'sci': 100, 'eng': 100}
key_to_extract = {'math', 'chem', 'sci'}

extracted_dict = {key: sub_dict[key] for key in sub_dict.keys() & key_to_extract}
print(extracted_dict)
print()
