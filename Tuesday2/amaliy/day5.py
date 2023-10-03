# text1 = "------------------------------------------------------------------\n\
#     \n-- Balans (1)\n\
# -- Valyuta ayirboshlash (2)\n\
# -- SMS xabar ulash (3)\n\
# -- O'tkazmalar (4)\n\
#     \n\
#     Xizmat turini tanlang(1/2/3/4): "

# text2 = "\n\n-------------------------------------------------------------------\n\
#     -- Valyuta ayirboshlash (2)\n\
#     -- so'mni dollarga (1)\n\
#     -- dollarni  so'mga (2)\n\
#     \n\
#     -- ortga (3)\n\
#     \n\
#     Tanlang(1/2): "

# balans = 3000000

# inform1 = input(text1)
# if inform1 == "1":
#     print(f"Balansda {balans} so'm bor")
# elif inform1 == "2":
#     tanlov = input(text2)
#     if tanlov == "1":
#         print("so'mni dollarga")
#     elif tanlov == "2":
#         print("Dollarni so'mga")


# print("hello wolrd")


# for a in range(10):
#     print(a)

# for nimadir in "Python":
#     print(1)


# print("hello world")
# print("")
# print("hello world")

# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i, end=" ")


# print("Python", end="")
# print("Django")


# r = 3
# L = 20

# print(f"Radius {r} ga teng va uzunligi {L} ga teng.")

# n = int(input("n = "))
# print(f"1 + 2 + ... + {n} = ", int(n * (n + 1) / 2))


# n = int(input("n = "))
# yigindi = 0
# # 1 + 2 + 3+ .. + n  ?

# for num in range(1, n + 1):
#     if num % 2 != 0:
#         yigindi += num  # yigindi = yigindi + num

# print(f"1 + 2 + ... + {n} = ", yigindi)

# a = 10
# del a # A toq son 2*n - 1 ---> n**2
# print(a)
# a = 0
# while False:
#     print(a, " Axis")
#     a += 1
# else:
#     print("Baraka savdo")

# n = int(input("n = "))
# a = 1
# while n > 0:
#     print(a)
#     print("n = ", n)
#     a += 1
#     n -= 1 # "8328382", "2838js,"

n = input("Raqam kiriting: ")

while not n.isdigit():
    n = input("Raqam kiriting dedim! --> ")

print(n)
