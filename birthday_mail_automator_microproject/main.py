import csv
import datetime as dt
import smtplib
from random import randint
import confidential

my_email = confidential.MAIL_ID
password = confidential.PASSWORD
current_date = dt.datetime.now()

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)

with open(r"birthdays.csv") as birthday_file:
    csv_reader = list(csv.reader(birthday_file))

for i in csv_reader[1:]:
    if str(current_date.month) == i[3] and str(current_date.day) == i[4]:
        with open(f"letter_templates/letter_{randint(1, 3)}.txt") as letter:
            msg = letter.read().replace("[NAME]", i[0])
            subject = f"Happy Birthday {i[0]}!!"
            connection.sendmail(
                from_addr=my_email, to_addrs=i[1], msg=f"Subject:{subject}\n\n{msg}")
            print(subject, msg, sep="\n")
            print("\n\n")

connection.close()
