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

# soz = input("So'z kiriting: ")

# if not soz.isalpha():
#     print("Hammasi harflardan iborat emas")
# else:
#     print("All is letters")

# shart1 = False
# shart2 = True
# shart3 = True
# shart4 = False

# if shart1:
#     if shart2:
#         print("shart1 va shart2 bajariladi")
#     elif shart3:
#         print("shart1 va shart3 bajariladi")
#     else:
#         print("shart1 bajariladi")
# elif shart4:
#     print("shart4 bajariladi")
# else:
#     print("Hech bir shart bajarilmaydi")


# matn = input("Matn kiriting :")

# if len(matn) > 50:
#     print("Long text")
# elif 20 < len(matn) < 50:
#     print("Medium text")
# else:
#     print("Small text")

# matn = input("Matn kiriting :")

# if len(matn) > 50:
#     print("Long text")
# elif len(matn) > 20 and len(matn) <= 50:
#     print("Medium text")
# else:
#     print("Small text")


son = int(input("Sonni kiriting: "))

if not son % 15:
    print("Fizz Buzz")
elif not son % 3:
    print("Buzz")
elif not son % 5:
    print("Fizz")
else:
    print("No comment")
