# 2
# matn = input("Matn kiriting: ")
# sanoq = 0
# result = ""
# word = ""
# for i in matn:
#     if i.isspace():
#         if sanoq > 5:
#             result += word[::-1] + " "
#             word = ""
#         else:
#             result += word + " "
#             word = ""
#         sanoq = 0
#     else:
#         sanoq += 1
#         word += i

# if sanoq > 5:
#     result += word[::-1]
# else:
#     result += word


# print(result)

# 3
# Bozor  5//2 = 2 Maktab (2,3)  6/2=3 samarqandd  (4,5)

# matn = input("Matn: ")

# if len(matn) % 2 == 1:
#     print(matn[len(matn) // 2])
# else:
#     start = (len(matn) // 2) - 1
#     stop = (len(matn) // 2) + 1
#     print(matn[start:stop])

# 4

# word = input("Word: ")
# result = ""
# sanoq = 1
# for i in word:
#     result += i * sanoq + "-"
#     sanoq += 1

# result += "\b "

# print(result)

# 5

# word = input("word: ")
# c = 0
# word = word.lower()
# letters = ""
# for i in word:
#     if i in letters:
#         c = 1
#         print("Izogramma emas")
#     letters += i

# if c == 0:
#     print("Izogramma")


# 1) list  .append() .insert(1,"Abdulloh")
# 2)tuple

# names = ["Asadbek", "Azizbek"]
# names.insert(1, "Abdulloh")
# c = 1
# for i in names:
#     print(f"{c}.{i}")
#     c += 1

# Set

# a = [1,2,3,True]  a = (1,2,3)  setnomi = {1,2,"hour"}

# print(type(setcha))

# setcha = set()

# setcha.add("python")
# setcha.add("python")
# setcha.add("django")

# for i in setcha:
#     print(i)
# print(qanadir[1]) # mumkin emas
# unique --> takrorlanmaydi

qanadir = {5, 4, 10, 2, 1}

print(qanadir)

a = {"java", "python", "flutter", "mobile"}
print(a)
