import smtplib

my_email = "pythoncraylie@gmail.com"
my_pw = "lz$oIOl84#Fu"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_pw)
    connection.sendmail(
        from_addr=my_email, to_addrs="scorelinebeast@gmail.com",
        msg="Subject: Hello""\n\n"
            "This is the body of my email."
    )
