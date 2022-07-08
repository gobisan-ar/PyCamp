import pandas

student_dict = {
    "student": ["Alan", "Peter", "Twinkle"],
    "score": [56, 76, 98]
}

student_df = pandas.DataFrame(student_dict)

# Loop through rows of data frame
for (index, row) in student_df.iterrows():
    print(index)
    print(row)

for (index, row) in student_df.iterrows():
    print(row.student)
    print(row.score)

for (index, row) in student_df.iterrows():
    if row.student == "Twinkle":
        print(row.score)
