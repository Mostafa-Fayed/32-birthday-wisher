import smtplib
import random
import datetime as dt

import sensitive_data

user_mail = sensitive_data.user_mail
recipient_mail = sensitive_data.recipient_mail
password = sensitive_data.password
subject = "Tuesday Motivational Quote "


weekday = dt.datetime.now().weekday()

if weekday == 1:
    with open("quotes.txt", "r") as quotes_file:
        quotes_list = quotes_file.readlines()
        random_quote = random.choice(quotes_list)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=user_mail, password=password)
            connection.sendmail(
                from_addr=user_mail,
                to_addrs=recipient_mail,
                msg=f"Subject:{subject}\n\n{random_quote}"
            )
else:
    print("Today is not Tuesday")
