import pandas
import datetime as dt
import random

birthday_dict = {}
letter_list = ["letter1.txt", "letter2.txt", "letter3.txt"]

# Read Birthday CSV
birthday_data = pandas.read_csv("birthdays.csv")
birthday_df = pandas.DataFrame(birthday_data)

for (index, row) in birthday_df.iterrows():
    birthday_dict.update({(row.month, row.day): (row.birthdayname, row.email, row.year, row.month, row.day)})

# Check for today birthdays
now = dt.datetime.now()
current_month = now.month
current_date = now.day

if (current_month, current_date) in birthday_dict:
    bday_name = birthday_dict[(current_month, current_date)][0]
    bday_email = birthday_dict[(current_month, current_date)][1]
    bday_letter = random.choice(letter_list)

# TODO: read the chosen letter and replace [name] with bday_name

# TODO: format and send e-mail