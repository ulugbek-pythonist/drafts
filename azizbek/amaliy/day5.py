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

# for i in {1, 2, 3}:
#     print(i)
# -----------------------------------------------------------------------------------


# pulot --> str       pulot(str)   >    hisob(int)

# for i in "Java":
#     print(i, end="/")

# ---------------------lists---------------------------


# newlist = list()
# # print(azizbek)
# # print(newlist)

# # print(dir(list))

# # print("Azizbek  ", azizbek)
# # print("Ulugbek  ", ulugbek)
# # print(len(azizbek))

# # ulugbek.clear()
# # print("Ulugbek  ", ulugbek)

# # print(dir(list))
# # print("Ulugbek  ", ulugbek)


# # print(ulugbek.count("css"))
# # print([2, 3, 4, 5, 644, 2, 3, 3, 3].count(4))

# # print(ulugbek.index("python"))

# # azizbek.extend(ulugbek)
# # azizbek = azizbek * 3212
# # print(azizbek)


# azizbek = ["python", "html", "css", "javascript"]
# ulugbek = azizbek.copy()
# azizbek.append("bootstrap5")
# ulugbek.insert(0, "Flutter")

# print(ulugbek)
# # ulugbek.pop()
# # ulugbek.pop()
# # ulugbek.remove("css")
# # ulugbek.pop(1)
# # ulugbek.sort(reverse=True)
# # ulugbek.reverse()
# print(ulugbek)

# matn = input("matn kiriting: ")

# sozlar = matn.split(" ")
# sozlar.reverse()
# print(" ".join(sozlar))

# ----------------------------Tuple----------------------

# a = ()
# a = tuple()
# a = 1, 2, "tuplecha"
# print(a)
# print(type(a))

# print(azizbek)
# print(type(azizbek))

# # print(dir(tuple))
# # print(azizbek.index("css"))
# # print(azizbek.index(7))
# # print(azizbek[-2])
# print(azizbek.count("Python"))

# azizbek = ("python", "java", "css", 7)

# value = input("Enter value: ")

# if azizbek.count(value) > 0:
#     print(f"index of {value} is ", azizbek.index(value))
# else:
#     print("Element not found...!!!")


# a = [12, 10, 20]
# print(a)
# a[1] = 17
# print(a)

# a = (1, 2, 3, 4, 5)

# a = list(a)
# print(a)
# # a[2] = 0
# del a[0:2]
# print(a)

# ---------------------------------------Set-------------------------------

setcha = set()
# setcha = {1}
# print(type(setcha))
# print(setcha)

setcha.add(2)
setcha.add(3)
setcha.add(4)
print(setcha)

# a = {1, 2, 2, 3, 3, 3, 4, 5, 5, 5}
# print(a)

# setcha.remove(5)
# setcha.discard(0)
print(setcha)
