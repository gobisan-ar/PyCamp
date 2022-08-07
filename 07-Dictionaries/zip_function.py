# Concatenate two lists index-wise

teams = ["India", "England", "NZ", "Aus"]
captains = ["Kohli", "Root", "Williaamson", "Smith"]

zipped = zip(teams, captains)
zipped_list = list(zipped)
print(zipped_list)

zipped = zip(teams, captains)
zipped_dict = dict(zipped)
print(zipped_dict)

print()


# Iterate multiple lists simultaneously

books = ["textbooks", "exercise books", "story book", "drawing books"]
prices = [100, 60, 90, 70]
quantities = [3, 2, 1, 4]

for book, price, quantity in zip(books, prices, quantities):
    print(f"You bought {quantity} {book} for ${price * quantity}")

print()


quantities = [10, 20, 30, 40]
fruits = ["Apples", "Mangoes", "Oranges", "Grapes"]

for quantity, fruit in zip(quantities, fruits[::-1]):
    print(quantity, fruit)


# Two Lists to Dictionary

country = ["USA", "France", "India"]
capital = ["Washington D.C.", "Paris", "New Delhi"]

zipped = zip(country, capital)
zipped_dict = dict(zipped)

print(zipped_dict)
