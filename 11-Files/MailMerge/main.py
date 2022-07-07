PLACE_HOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names_list = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    message = letter_file.read()
    for name in names_list:
        name = name.strip()
        new_letter = message.replace(PLACE_HOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)




