
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1.lower() + name2.lower()

love_count = 0
true_count = 0

love_count += combined_string.count("l")
love_count += combined_string.count("o")
love_count += combined_string.count("v")
love_count += combined_string.count("e")

true_count += combined_string.count("t")
true_count += combined_string.count("r")
true_count += combined_string.count("u")
true_count += combined_string.count("e")

love_score = str(true_count) + str(love_count)
love_score = int(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")


