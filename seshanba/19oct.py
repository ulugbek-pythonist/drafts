# # 1-misol
# my_list = ["python", "java", "swift", "django", "fastapi", "mysql"]
# print(my_list[4])

# # 2-misol
# my_list = ["python", "java", "swift", "django", "fastapi", "mysql"]
# print(my_list[2])

# # 3-misol
# my_list = ["python", "java", "swift", "django", "fastapi", "mysql"]
# print(my_list[5])

# # 4-savol
# my_list = ["python", "java", "swift", ["django", "fastapi"], "mysql"]
# print(my_list[3][0])

# # 5-savol
# my_list = ["python", "java", "swift", ["django", "fastapi"], "mysql"]
# print(my_list[3][1])

# # 6-savol
# my_list = ["python", "java", "swift", [["django", "fastapi"], "mysql"], "aiogram"]
# print(my_list[3][0][1])

# # 7-savol
# my_list = ["python", "java", "swift", [["django", "fastapi"], "mysql"], "aiogram"]
# my_list[3][0][1] = "pytube"
# print(my_list)

# # 8-savol
# my_list = ["python", "java", "swift", [["django", "fastapi"], "mysql"], "aiogram"]
# my_list[3][1] = "postgresql"
# print(my_list)

# # 9-savol
# my_list = ["python", "java", "swift", [["django", "fastapi"], "mysql"], "aiogram"]
# print(my_list[0:2])

# # 10-savol
# my_list = ["python", "java", "swift", [["django", "fastapi"], "mysql"], "aiogram"]
# print(my_list[3][0])

# 11

# a = ["python", "java", "swift", [["django", "fastapi"], "mysql"], "aiogram"]

# print(a[::2])

# 12

# a = ["sariqdev", "modirdev", "pdp", "axis"]

# b = input("Enter anything: ")

# a.append(b)
# print(a)

# 13

# a = ["sariqdev", "modirdev", "pdp", "axis"]

# b = input("Enter anything: ")

# a.insert(0, b)
# print(a)

# 14

# a = ["sariqdev", "modirdev", "pdp", "axis"]

# b = input("Enter anything: ")

# a.insert(2, b)
# print(a)

# a = ["elixir", "scala", "java", "android"]

# a.pop(0)
# print(a)

# a = ["Farrux", "Abbos", "Begzod", "Alijon"]

# a.sort()
# print(a)

# a = [1, 2, 3]
# b = [20, 30, 40]
# c = a + b
# print(c)

# a = [1, 2, 3]
# b = ["red", "green", "blue"]
# c = a.extend(b)
# print(a)

# son = int(input("son = "))

# a = []

# a.extend(range(2, son + 1, 2))
# print(a)


# a = "Python Java Bootstrap"

# print(a.split())


# a, b, c = input("a, b, c ni kiriting: ").split()

# print(a)
# print(b)
# print(c)

# a, b, d = [1, 2, 3]
# print(a, b)


# primitive types: int,str,bool,float

# collection types: list, tuple, set

# print(dir(tuple))

# my_tuple = 1, 2
# print(type(my_tuple))

# a = (1, 2, "Axis", (1, 2, ["user", "admin"]))

# # print(a[3][2][1])
# # print(a[1:3])

# print(a.index(1))
# print(a.count(1))

a = set()

# print(type(a))
# print(a)
# a.add("Muhammaddiyor")
# a.add("Muhammaddiyor")
# a.add("Samandar")
# print(a)

# usernames = {"user1", "user2", "user3"}

# print(usernames)
# n = int(input("How many usernames do you add: "))
# for i in range(n):
#     a = input("Add user: ")
#     usernames.add(a)
# print(usernames)

# a = {1, 1, 1, 1, 10, 2, 1, 2, 2, 3}

# print(a)

# a = {1, 2, 3}
# b = {2, 3}
# print(b.issubset(a))

# for i in {1, 2, 3}:
#     print(i)
