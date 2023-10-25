import smtplib

receiver = input("Kimga: ")
subject = input("Mavzu: ")
body = input("Xabar: ")

sender = "edvaardhouse@gmail.com"

parol = "zvuh yjsz nnmk ofso"

message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(sender, parol)
    print("Ulandi...")

    server.sendmail(sender, receiver, message)
    print("Jo'natildi!")
except smtplib.SMTPAuthenticationError:
    print("Ulanolmadi...")
