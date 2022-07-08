numbers = [1, 2, 3]
print(numbers)

new_list = []
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Loki"
new_list = [letter for letter in name]
print(new_list)

range_list = [num * 2 for num in range(1, 5)]
print(range_list)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num % 2 == 0]
print(result)

# Conditional list comprehension
names = ["Bruce", "Loki", "Peter", "Steve", "Tony", "Thor"]

troops = [name for name in names if len(name) < 5]
print(troops)

caps = [name.upper() for name in names if len(name) >= 5]
print(caps)


with open("file1.txt") as file1:
    file1_data = file1.readlines()

with open("file2.txt") as file2:
    file2_data = file2.readlines()

result = [int(num) for num in file1_data if num in file2_data]
print(result)
