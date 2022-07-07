# Method - 01: Open File
# Read File
file = open("my_file.txt")

contents = file.read()
print(contents)

file.close()


# Method - 02: Open File
# Read File
# File Open Mode: r
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)


# Write File
# File Open Mode: w
# Overwrite
with open("my_file.txt", mode="w") as file:
    file.write("New text 01.")


# Write File
# File Open Mode: a
# Overwrite
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text 02.")


# Create File
with open("new_file.txt", mode="w") as file:
    file.write("New file.")