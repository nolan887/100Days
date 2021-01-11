import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

data_dictionary = data.to_dict()
print(data_dictionary)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))


# Average Temperature

# temp_count = 0
# temp_total = 0
#
# for temp in temp_list:
#     temp_count += 1
#     temp_total += temp
#
# temp_avg = round(temp_total / temp_count)


# or, easier:
# temp_avg = sum(temp_list) / len(temp_list)


# # or, easiest:
# temp_avg = data["temp"].mean()
# print(f"Average temperature: {temp_avg} deg C")



# # Maximum Temperature
# temp_max = data["temp"].max()
# print(f"Max temperature: {temp_max} deg C")



# # Get data in columns
# print(data["condition"])
# # this does this same thing, different syntax
# print(data.condition)


# # Get data in rows
# print(data[data.day == "Monday"])

# # Challenge: Print the row that has the highest temperature
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * (9/5) + 32
# print(f"Converted Monday temperature is: {monday_temp_F} deg F")

# # Creating my own dataframe from scratch
# my_data_dictionary = {
#     "family": ["Charles", "Ashley", "Kai", "Brady", "Khaleesi", "Luther"],
#     "age": [33, 33, 0.7, 11, 9, 2]
# }
#
# new_data = pandas.DataFrame(my_data_dictionary)
# print(new_data)
#
# new_data.to_csv("my_new_data.csv")