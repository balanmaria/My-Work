import os
import smtplib

MY_EMAIL=os.environ["USER"]
MY_PASSWORD=os.environ["PASSWORD"]

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() #make connection secure
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:Security breach\n\nDear Client,\n\nOur technical support and customer department has recently suspected activities in your account.\n\nYour Huawei account has been limited because we've noticed significant changes in your account activity. As your payment processor, we need to understand these change better.\n\nWe're always concerned about our customers security so please let me know where we can contact you for solve this problem\n\nThank you!")