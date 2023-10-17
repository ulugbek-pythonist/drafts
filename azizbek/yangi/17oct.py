# azizbe = [1, 2, 3, (1, 2, 3), ["py", "exe"]]

# print(azizbe[3][1])
# print(azizbe[4][0])

# b = (1, 2, 3)

# print(
#     (
#         1,
#         2,
#         3,
#         (
#             1,
#             2,
#             3,
#             (
#                 "python",
#                 ["java", "kotlin"],
#             ),
#         ),
#     )[3][
#         3
#     ][1][1]
# )
# Sets


# for i in a:
#     print(i, end=",")
# print("\b ")

# c = a.union(b)

# print(list(c))

# a = {1, 2, 3}
# b = {-1, -2, 3}
# print("a origin: ", a)
# a.intersection_update(b)
# print("a: ", a)
# print("b origin: ", b)
# b.difference_update(a)
# print("b: ", b)

# print("union: ", a.union(b))
# print("intersection(kesishma): ", a.intersection(b))
# print("difference: ", b.difference(b))

# a = {"Python", "Django", "FastAPI", "API", "aiogram", "turtle"}

# b = {"Python", "Django", "FastAPI", "pygal", "pytube"}

# print(a)
# qaysi = input("Qaysi birini o'chirasiz: ")
# a.discard(qaysi)
# print(a)


# Dictionaries
bombosh = dict()
# print(type(bombosh))

#  {kalit:qiymat,kalit1:qiymat1,...}

# lugat = {"olma": 1, "nok": "pear"}


# # accessing elements(key,value pairs) kalit-qiymat juftliklari

# print(poytaxtlar["taj"])

# print("-----------------------------------------")
# print("--------- Fruits dictionary--------------")
# print("-----------------------------------------")

# mevalar = {
#     "pear": "nok",
#     "apple": "olma",
#     "banana": "banan",
#     "peach": "shaftoli",
#     "pineapple": "ananas",
#     "melon": "qovun",
#     "watermelon": "tarvuz",
# }

# meva = input("Meva nomini kiriting: ")
# # if meva in mevalar.keys():
# #     print(f"{meva} --- {mevalar[meva]}")
# # else:
# #     print("Lug'atda yo'q")

# print(mevalar.get(meva, "Bunday kalit yo'q"))

# adding elements

# lugat[yangi_key] = value

poytaxtlar = {
    "uzb": "Tashkent",
    "kaz": "Nursulton",
    "taj": "Dushanbe",
    "rus": "Moskva",
}


davlat = input("Davlat nomi: ")

if davlat in poytaxtlar.keys():
    print("Poytaxti: ", poytaxtlar[davlat])
    ask = input(
        "Delete? \n\
Yes(1)\n\
No (0)\n\
\nTanla: "
    )
    if ask == "1":
        del poytaxtlar[davlat]
    else:
        pass
else:
    poytaxt = input("Men bilmayman, o'zing kirit: ")
    poytaxtlar[davlat] = poytaxt
    print("Ro'yhat yangilandi: ")

for kalit, qiymat in poytaxtlar.items():
    print(kalit, qiymat, sep=" --- ")
