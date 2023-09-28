#  day2
# 1

# ......

# 2

# from math import sqrt as ildiz

# son = int(input("Sonni kiriting: "))
# diapazon = round(ildiz(son))
# b_soni = 0

# for i in range(1, diapazon + 1):
#     if son % i == 0:
#         b_soni += 1

# if b_soni > 1:
#     print("murakkab son")
# else:
#     print("Tub son")

# 3
# matn = input("Matn kiriting: ")

# # 1) .count()
# # print("Azizbek".count("z"))

# print(
#     matn.lower().count("a")
#     + matn.lower().count("e")
#     + matn.lower().count("i")
#     + matn.lower().count("o")
#     + matn.lower().count("u")
#     + matn.lower().count("o'"),
#     " ta bo'g'in bor",
# )

# 2) in

# 4
# soz = input("So'z kiriting: ")

# if soz == soz[::-1]:
#     print("Palindrom")
# else:
#     print("Palindrom emas")


# for i in range(1, 21):
#     if i % 5 == 0:
#         continue
#     print(i)

# lists --> ro'yxat
# collection/sequence types
# constructor --> a = list() | ([])

# print(type(users))
# a = "sams", "hixwj"
# print(type(a))
# a = (1, 2, 3, True, "string")

# for i in "Python":
#     print(i, end=";")

# for user in users:
#     print(user)

# print("Python"[::-1])

# print(users[3])
# print(users[-2])

# print(users[:2])
# print(users[::-1])

# print(users[1:4:2])
# print(type(users[0:1]))
# print(type(users[0]))

# print(users)
# users.append("Malika")
# print("After appending Malika --> ", users)
# users.insert(1, "Abdulloh")
# print("After inserting Abdulloh --> ", users)
# users.remove("Malika")
# print("After removing Malika --> ", users)
# a = "word"
# print(a.upper())
# print(a)
# users.pop(1)
# print(users)
# users.sort()
# users.insert(0, "Bahromjon")
# print(users)
# print(sorted(users))
# print(users)


users = ["Samandar", "Oyatulloh", "Ulug'bek", "Abdulaziz", "Xurshidbek"]
# users.sort(reverse=True)
# print(users)
# users.sort()
# print(users)
# print(dir(list))

# print("aaabbbcdef".count("c"))

# print(users.count("samandar"))

# print("hello " + "world")

# people.clear()
# del people
# people = 1

# people = users + accounts
# print(people)
# people.extend(["Asadbek", "Maliika", "Aziza"])
# print(people)
# print(people.index("Abdulloh", 0, 7))

# tuple -->
# a = tuple()
# print(a)
# print(dir(tuple))

# print(sonlar.count(2))
# print(sonlar.index(5, 3))
# print(len(sonlar))

# accounts = ["Abdulloh", "Bahromjon", "O'ktamjon"]

# accounts[1] = "Samandar"

# print(accounts)
# sonlar = (2, 34, 5, 6, 7, 8, 5)
# print(sonlar[3::-1])

# a = ("a",)
# print(type(a))
