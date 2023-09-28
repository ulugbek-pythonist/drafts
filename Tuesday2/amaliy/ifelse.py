# A
# 1

# print("Ulug'bek".endswith("jon"))
# print("Ulug'bek".startswith("ul"))

# familiya = input("familiya kiriting: ")

# if familiya[-1].lower() == "v":
#     print("erkak kishi")
# elif familiya[-1].lower() == "a":
#     print("ayol kishi")

# if familiya.endswith("v"):
# print("erkak kishi")
# else:
# print("ayol kishi")


# print("phone"[::-1])


# word = input("Biror nima kiriting: ")

# if word == word[::-1]:
#     print("Palindrom")
# else:
#     print("Palindrom emas")

# print(bool(-1))


# a = int(input("Number: "))

# if a % 3 == 0 and a % 5 == 0:
#     print("Bingo")


# a = int(input("Number: "))

# if (a % 3 == 0) or (a % 5 == 0):
#     print("Bingo")

# soz
# 1) Bosh harf b-n boshlansin
# 2) Uzunligi 10 dan katta bo'lsin
# "Awesome!"


# soz = input("So'z kiriting: ")

# if soz[0].isupper() or len(soz) > 10:
#     print("Awesome!")


# soz = input("So'z kiriting: ")

# if not len(soz) > 50:
#     print("Medium")
# elif len(soz) > 50:
#     print("Long")

soz = input("So'z kiriting: ")

if not soz.isalpha():
    print("Hammasi harflardan iborat emas")
else:
    print("All is letters")
