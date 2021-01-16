# Re-code of Day 26 NATO Alphabet project

import pandas
dict_is_on = True

nato_data = pandas.read_csv("nato_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

while dict_is_on:
    word_to_translate = str.upper(input("What word would you like translated?: "))
    try:
        phoenetic = [nato_dict[letter] for letter in word_to_translate]
    except KeyError:
        print("Characters entered were not in the NATO dictionary, please try again.")
    else:
        print(phoenetic)