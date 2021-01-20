import pandas
import datetime as dt
import random
import smtplib

PLACEHOLDER = "[NAME]"
OUTPUT_LINK = "./wishes-sent/"

my_email = "pythoncraylie@gmail.com"
my_pw = ""

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
    bday_letter = "letter_templates/" + str(random.choice(letter_list))

    with open(bday_letter, "rt") as ltr:
        letter_contents = ltr.read()
        new_wish = letter_contents.replace(PLACEHOLDER, bday_name)
        with open((OUTPUT_LINK + bday_name + "_email.txt"), mode="w") as completed_email:
            completed_email.write(new_wish)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_pw)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg=f"Subject: HBD!\n\n {new_wish}".encode("utf-8"))
