# Extend nested list with sub list

list_1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

print(list_1[2])
print(list_1[2][1])
print(list_1[2][1][2])
print()

list_1[2][1][2].extend(sub_list)
print(list_1)
print()

list_1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

list_1[2][1][2].append(sub_list)
print(list_1)
print()


# Remove all the occurrences of an element from a list

list_1 = [10, 15, 20, 15, 32, 54, 15]

while 15 in list_1:
    list_1.remove(15)
    print(list_1)

print()
