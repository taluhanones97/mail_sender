import smtplib

my_email="taluhan07@gmail.com"
password="*******************"


import datetime as dt

now=dt.datetime.now()
today=now.weekday()

quotes_list=list()
with open(file="quotes.txt",mode="r") as file:
    quotes_list=file.readlines()

import random

message=random.choice(quotes_list)
print(message)

while True:
    if today==1:
        with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="otaluhan@gmail.com",
                                msg=f"Subject:MOTIVATION\n\n {message}")