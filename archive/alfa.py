# shart = False
# while shart:
#     print("code")
#     print("code")
#     print("code")
# else:
#     print("while ning else")


# if shart:
#     print("code")
#     print("code")
#     print("code")

# print("....")
# print("....")
# print("....")


# n = int(input("n = "))

# for e in range(1, n + 1):
#     print(e, end=",")
# print("\b.")


# n = int(input("n = "))
# a = 1
# while n > 0:
#     if a % 2 != 0: # agar a toq son bo'lsa
#         print(a) # chop et!
#     a += 1 # a ni qiymatini orttiryapman
#     n = n - 1 # n ni qiymatini kamaytiryapman


# break va continue


# n = int(input("n = "))

# while True:
#     print(n)
#     n += 1
#     if n == 20:
#         break


# matn = input("Matn kiriting: ")

# matn = (
#     matn.replace("a", "")
#     .replace("o", "")
#     .replace("e", "")
#     .replace("u", "")
#     .replace("i", "")
# )
# matn = (
#     matn.replace("A", "")
#     .replace("O", "")
#     .replace("E", "")
#     .replace("U", "")
#     .replace("I", "")
# )
# print(matn)


# matn = input("Matn: ")
# sanoq = 0
# result = ""
# word = ""
# for u in matn:
#     if u.isspace():
#         if sanoq > 5:
#             result += word[::-1] + " "
#             word = ""
#         else:
#             result += word + " "
#             word = ""
#         sanoq = 0
#     else:
#         sanoq += 1
#         word = word + u

# if sanoq > 5:
#     result += word[::-1] + " "
#     word = ""
# else:
#     result += word + " "
#     word = ""


# print(result)


# soz = input("So'z: ")
# counter = 0

# for a in soz:
#     counter += 1
#     print(a * counter, end="-")
# print("\b ")

# soz = input("So'z: ")
# counter = 0
# long = len(soz)

# while long > 0:
#     counter += 1
#     print(soz[counter - 1] * counter, end="-")
#     long -= 1
# print("\b ")

# soz = input("So'z: ")
# letters = []
# c = 0

# for harf in soz:
#     if harf in letters:
#         c = 1
#         print("Izogramma emas")
#         break
#     letters.append(harf)

# if c == 0:
#     print("Izogramma")
