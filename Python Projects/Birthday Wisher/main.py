#TODO imports
import datetime as dt
import pandas
import random
import smtplib
import os

#TODO crediantials

my_gmail = os.environ.get("GOOGLE_USER")
gmail_password = os.environ.get("GOOGLE_PASS")


now = dt.datetime.now()
today = (now.month,now.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]) :data_row for (index,data_row) in data.iterrows()}

if today in birthday_dict :
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        birthday_person = birthday_dict[today]
        contents = letter_file.read()
        final_content = contents.replace("[NAME]",birthday_person["name"])
    #TODO send using smtp
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail,password=gmail_password)
        connection.sendmail(from_addr=my_gmail,to_addrs=birthday_person["email"],
                            msg=f"Subject:Wishing you Happy Birthday !\n\n{final_content}"
        )