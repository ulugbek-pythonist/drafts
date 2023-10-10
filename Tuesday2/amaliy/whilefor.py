# import time

# time.sleep(3)

# print("Time is up!")

# for i in range(11, 0, -1):
#     print(i)
# else:
#     print("boom!")

# for a in "Axis academy":
#     print("bu for loop")
#     print("bu while loop emas")

# print("the end")


# son = int(input("Sonni kiriting: "))

# for num in range(1, son + 1):
#     print(num, end=",")
# print("\b ")
# print("Oyatulloh", end=",")
# print("Zikrulloh", end=" ")
# print("Abdulaziz")


# son = int(input("Sonni kiriting: "))

# for num in range(1, son + 1,):
#     if num % 2 == 0:
#         print(num, end=",")
# print("\b ")


# for a in range(-20, 8):
#     print(a, end=", ")
# print("\b\b ")


# son = int(input("Sonni kiriting: "))

# for num in range(1, son + 1):
#     if num % 3:
#         print(num, end=",")
#     else:
#         print("Bingo", end=",")
# print("\b ")


# for harf in "text":
#     print(harf)
# else:
#     print("Else qismi")


# a + .. + b = ?

# if a > b:
#     for i in range(b, a + 1):
#         if i % 2 == 0:
#             yigindi += i
# else:
#     for i in range(a, b + 1):
#         if i % 2 == 0:
#             yigindi += i

# print(f"Natija = {yigindi}")


# a = int(input("a = "))
# b = int(input("b = "))
# yigindi = 0

# for c in range(min(a, b), max(a, b) + 1):
#     if c % 2 == 0:
#         yigindi = yigindi + c  # yigindi += c

# print(yigindi)


# a = int(input("a = "))
# counter = 1

# while a > 0:
#     print("Meni to'xtat!")
#     print(counter)
#     counter += 1
#     a -= 1

# print("......")
# print("......")
# print("......")

# a = 3

# print("a = ", a)

# a = a + 4  # a += 4
# print("a = ", a)
# # a % n -->
# a %= 3
# print("a = ", a)


# # print() len() bin() max() round()   .upper() .lower()
# # .isdigit()  ---> "28292992" -> True  aks holda False

# raqam = input("Raqam kiriting: ")

# while not raqam.isdigit():
#     raqam = input("Raqam kiriting: ")

# print(f"Siz {raqam} ni kiritdingiz")


def truncate(text, length=0):
    try:
        return text[:length] + "..." if len(text) > length else text
    except Exception:
        return ""
