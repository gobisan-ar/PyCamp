# Absolute file paths
with open("D:\DevBase\Project_Data_Space\PyCamp\Files\Vault\secretdata.txt") as file:
    contents = file.read()
    print(contents)


# Relative file paths
with open("Vault/secretdata.txt") as file:
    contents = file.read()
    print(contents)