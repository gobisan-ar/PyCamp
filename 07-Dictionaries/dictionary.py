programming_dictionary = {
    "Bug": "A coding error in a computer program.",
    "Function": "A chunk of code that can be called over and over again.",
}

# Retrieving items from dictionary.
print(programming_dictionary["Bug"])

# key error
# programming_dictionary["Syntax"]

# Adding new items to dictionary.
programming_dictionary["Loop"] = "A loop is used to repeat a block of code until the specified condition is met."
print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# Edit item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)




