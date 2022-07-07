import pandas

data = pandas.read_csv("weather_data.csv")

# DataFrame
print(type(data))
print(data)

print("\n")

# Series
print(type(data["temp"]))
print(data["temp"])
