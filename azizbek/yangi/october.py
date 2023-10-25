# try:
#     print("azizbek")
#     a = int("2a")
#     print(2 / 0)
# except ValueError:
#     raise ValueError
# except IndentationError:
#     print("Indentatsiyani qo'y")
# except ZeroDivisionError:
#     print("Nolga bo'lma")
# finally:
#     print("Finally bloki")

# print(round(12.34234324, 2))

# a = {1,2,3,4,5} # superset  a.issuperset(b)
# b = {2,0}  # subset   b.issubset(a)

# Functions


# def xushkelding():
#     # codes
#     """Bu funksiya nimadir bajaradi rostdan"""
#     print("Assalomu alaykum!")
#     print("O'zbekistonga xush kelding o'g'lon!")
#     print("....!")  # end of lines


# xushkelding()

# a = [32, 45, 12, 23]

# a = sorted(a)
# print(a)
# void funksiya


# def aniqlayman(son: int):
#     """Juft yoki toqligini aniqlayman"""
#     if son % 2 == 0:
#         print("Juft son")
#     else:
#         print("Toq son")


# number = int(input("Sonni kiriting: "))
# aniqlayman(son=number)


# def kotta(a, b):
#     if a > b:
#         print(f"{a} katta")
#     elif a == b:
#         print("Teng")
#     else:
#         print(f"{b} katta")


# kotta(12, 23)


# def info(yosh=13, ism="Azizbek"):
#     print(f"{ism} {yosh} yoshda.")


# info(ism="Tolibjon")


# def is_palindrom(text):
#     text = str(text)
#     if text == text[::-1]:
#         return True
#     return False


# print(is_palindrom(121))


# def azizbek(num: int):
#     total = 0
#     for i in range(1, num + 1):
#         total += i

#     return total


# diapazon = azizbek(15)

# print(diapazon)


# def teskari(soz):
#     soz = str(soz)
#     return soz[::-1]


# word = teskari(28377837)

# print(word)


# def is_prime(n: int):
#     pass
#     tub = {2, 3, 5, 7, 9}

#     if n in tub:
#         return True

#     b_soni = 0

#     for i in range(1, n + 1):
#         if n % i == 0:
#             b_soni += 1
#         if b_soni > 2:
#             return False

#     return True


# print(is_prime(837493274932))
