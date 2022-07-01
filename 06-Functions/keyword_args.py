def greet_user(name, location):
    print(f"Hello {name}")
    print(f"What is it  like in {location}")
    print()

greet_user("Gary", "Gotham")

greet_user("Gotham", "Gary")

greet_user(location="Gotham", name="Gary")