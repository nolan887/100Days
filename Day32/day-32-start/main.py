# import smtplib
#
# my_email = "pythoncraylie@gmail.com"
# my_pw = ""
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_pw)
#     connection.sendmail(
#         from_addr=my_email, to_addrs="scorelinebeast@gmail.com",
#         msg="Subject: Hello""\n\n"
#             "This is the body of my email."
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# nyr = now.year
# nmo = now.month
# nda = now.day
# nwd = now.weekday()
# print(nyr, nmo, nda)
# print(nwd)

import smtplib
import datetime as dt
import random

my_email = "pythoncraylie@gmail.com"
my_pw = ""

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pw)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: Monday Motivation\n\n QOTD: {quote}".encode("utf-8"))