import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")


# Heads or tails
random_side = random.randint(0, 1)

if random_side == 1:
    print("Heads")
else:
    print("Tails")