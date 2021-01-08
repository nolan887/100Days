# how many gray, cinnamon, and brown squirrels?
# make a CSV with the color and a count from the existing CSV
#
# Primary Fur Color

import pandas

squirrel_colors = ["Gray", "Cinnamon", "Black"]

data = pandas.read_csv("squirrel_count.csv")

gray_fur = data[data["Primary Fur Color"] == "Gray"]
black_fur = data[data["Primary Fur Color"] == "Black"]
cinnamon_fur = data[data["Primary Fur Color"] == "Cinnamon"]

gray_count = len(gray_fur)
black_count = len(black_fur)
cinnamon_count = len(cinnamon_fur)

color_list = [gray_count, cinnamon_count, black_count]

my_color_dictionary = {
    "Primary Fur Color": squirrel_colors,
    "Amount of Squirrels": color_list
}

my_complete_colors = pandas.DataFrame(my_color_dictionary)
print(my_complete_colors)
my_complete_colors.to_csv("Charles Squirrel Color.csv")