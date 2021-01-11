import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_data = pandas.read_csv("nato_alphabet.csv")

nato_df = pandas.DataFrame(nato_data)
nato_dict = {}

for (index, row) in nato_df.iterrows():
    nato_dict.update({row.letter: row.code})

print(nato_dict)
phoenetic = ""

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word_to_translate = str.upper(input("What word would you like translated?: "))

letters_list = [letter for letter in word_to_translate]
for letter in letters_list:
    phoenetic += nato_dict[letter]
    phoenetic += " "
print(phoenetic)