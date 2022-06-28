import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_index = random.randint(0, len(names) - 1)
treat = names[random_index]

# treat = random.choice(names)

print(f"{treat} is going to pay the bill today!")
