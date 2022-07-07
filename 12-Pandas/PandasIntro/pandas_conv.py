import pandas

data = pandas.read_csv("weather_data.csv")


# Convert DataFrame to dictionary.
data_dict = data.to_dict()
print(data_dict)


# Convert series to list
temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list))