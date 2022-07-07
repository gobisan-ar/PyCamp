import pandas

data = pandas.read_csv("weather_data.csv")

# Get data in column
print(data["condition"])
print(data.condition)


# Get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = int(monday.temp)
monday_temp_F = monday_temp * (9/5) + 32
print(monday_temp_F)
