import pandas

data = pandas.read_csv("weather_data.csv")


# Calculate average temperature
avg_temp = data["temp"].mean()
print("{:.2f}".format(avg_temp))


# Find maximum temperature values
max_temp = data["temp"].max()
print(max_temp)

