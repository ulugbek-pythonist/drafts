# d = {4, 1024, 5, 7, 1, 2}
# print(d)
# print(id(d))
# c = {"c", "b", "a"}
# print(id(c))
# print(c)

# # print(dir(set))
# # d.update(c)
# print(d)
# da = isinstance(d, set)
# print(da)

# b = [1, 2, 3, 4, 5, 6, 7, 8]
# a = slice(1, 7, 2)
# print(b[a])

# import os

# try:
#     os.remove("unititled.txt")
#     print("File moved")
# except Exception as e:
#     print("Error: {}".format(e))
# import smtplib

# sender = "samternary@gmail.com"
# receiver = "johnternary@gmail.com"
# password = "ttzl ezhq bpal vzev"
# subject = "just"
# body = "Assalamu alaykum!"

# xabar = f"""From; {sender}
# To: {receiver}
# Subject: {subject}\n
# {body}
# """

# servercha = smtplib.SMTP("smtp.gmail.com", 587)
# servercha.starttls()

# try:
#     servercha.login(sender, password)
#     print("Logged in...")
#     servercha.sendmail(sender, receiver, xabar)
#     print("E-mail has been sent")
# except Exception as e:
#     print(f"{e}")

for i in {1, 2, 3}:
    print(i)
