# sodda turlar

# a = 5
# b = "Uzb"
# c = True
# rating = 3.75

# kolleksion turlar

# a = ["axis", 1, 2, 3.7, False,["django","spotify",["secret","key"]]]

# printing

# print(len(a))
# for sardorbek in a:
#     print(sardorbek,end=" | ")

# elementlariga murojaat qilish va o'zgartirish

# print(a[-1])
# print(a[3]) 
# print(a[-1][1])
# print(a[-1][-1][0])

# a[0] = "edu"
# a[-1][1] = "audio"
# a[-1][-1][0] = "public"
# print(a)
# a = ["axis", 1, 2, 3.7, False,["django","spotify",["secret","key"]]]
# b = ["javascript","css","html"]
# element qo'shish

# a.append("java")
# a.insert(5,"flutter")
# a.extend(range(10))
# c = a + b
# print(c)
# a[-1][2].append("box")
# print(a)



# a = ["axis", 1, 2, 3.7, False,"django","spotify","secret","key"]

# slicing  kesib olish
# print(a[::3])
# o'chirish
# a.pop(5)
# print(a)
# a.remove("django")
# print(a)
# del a[5]
# print(a)
# a = ["axis","secret","django","spotify","secret","key"]

# try:
#     print(a.index("secrets"))
# except Exception:
#     print("Bunday element yo'q")

# a.clear()
# b = a.copy()
# print(b)
# print(a.count("secret"))
# a = [100,20,-5,7.9,18,39,27]
# # a.sort(reverse=True)
# # a.sort()
# a.reverse()
# print(a)

# soz = input("So'zlar: ").split()
# soz.reverse()
# print(" ".join(soz))

# ---------------------------------------------------------
# b = ("py", "exe", "doc", "ppt")

# printing

# print(b)
# for i in b:
#     print(i)

# print(b[1:3])

# b = ("py", "exe", "doc", "ppt",("pop","remove","del"))
# del b # tuple o'chadi
# print(b[-1][-1])

# b = ("py", "exe", "doc", "ppt","ppt","remove","del")

# print(b.count("py")) # 1
# print(b.index("ppt"))  # 3

# ---------------------------------------------------------
# c = {3, 4, "Termiz", "Buxoro"}
# # c = set()  # bo'sh set
# for i in c:
#     print(i)

# qo'shish
# c.add("Baraka choyxonasi")
# print(c)

# o'chirish
# c.remove(3)
# print(c)
# c = list(c)

# a = [1,2,2,21,11,11,11,1]

# a = set(a)
# print(a)


# c = {3, 4, "Termiz", "Buxoro"}
# try:
#     c.remove("termiz")
# except KeyError:
#     print("unaqa element yo'q oma")

# c.discard(5)
# print(c)
# usernames = {"azizbek","samandar"}
# usernames.pop()
# usernames.clear()
# print(usernames)
# import time

# usernames = set()

# for i in range(1,11):
#     usernames.add(f"user{i}")
#     time.sleep(2)
#     print(usernames)


# a = {1,2,3}
# b = {2,3,4}

# print(a.union(b))  # birlashmasi
# print(a.intersection(b))  # kesishmasi
# print(a.difference(b))  # ayirmasi
# print(b.difference(a))  # ayirmasi
# print(b.symmetric_difference(a))  # simmetrik ayirmasi


# a.update(b) # union ni qiymati bilan yangilaydi
# a.intersection_update(b)
# a.difference_update(b)
# a.symmetric_difference_update(b)
# print(a)




# ---------------------------------------------------------

# a = {}
# b = dict()

# a["suv"] = "water"
# a["olma"] = "don't take"
# print(a)
# a["olma"] = "apple"
# print(a)

# del a["olma"]

# print(a)

# sardorbek = {
#     "name": "Sardorbek",
#     "age": 16,
#     "address": "Yuksalish st.",
#     "is_student": True,
#     "more":{"tel":"+99872822727","username":"user1"},
# }

# print(sardorbek)

# for i in sardorbek.keys():
#     print(i)

# for i in sardorbek.values():
#     print(i)

# for key,val in sardorbek.items():
#     print(f"{key} --> {val}")

# print(sardorbek["more"]["tel"])
