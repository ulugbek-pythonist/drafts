import smtplib

receiver = input("To whom: ")
subject = input("Subject of message: ")
body = input("Message: ")

sender = "johnternary@gmail.com"
password = "mqsm pcxn jqsa niww"

message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(sender, password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print("Unable to log in!")
