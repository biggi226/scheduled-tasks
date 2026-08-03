# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import datatime as dt
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

def sender(email, message):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=email,
                            msg=f"Subject:Happy Birthday!\n\n{message}")

this_month = dt.datetime.now().month
today = dt.datetime.now().day
my_birthday_db = pandas.read_csv("birthdays.csv")
birthdays_db = my_birthday_db.to_dict(orient="records")

my_wish_list = []
for smth in birthdays_db:
    if smth["month"] == this_month and smth["day"] == today:
        letters_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(letters_path, "r") as quote_file:
            my_email_content = quote_file.read()
            my_email_content = my_email_content.replace("[NAME]", smth["name"])
            sender(smth["email"], my_email_content)
