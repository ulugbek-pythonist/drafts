from math import sqrt as ildiz


def is_tub(son):
    son = int(son)
    diapazon = round(ildiz(son))
    b_soni = 0

    for i in range(1, diapazon + 1):
        if son % i == 0:
            b_soni += 1
    if son > 0:
        if son == 1:
            return False
        elif b_soni > 1:
            return False
        else:
            return True
    return "Natural son kiriting"


n = int(input("Sonni kiriting: "))
diapazon = n
boluvchilar = []

if is_tub(n):
    print("Bu tub son: ", f"{n} = 1*{n}")
else:
    pass
    for i in range(2, diapazon):
        if is_tub(i):
            while n % i == 0:
                boluvchilar.append(i)
                n /= i

setcha = set(boluvchilar)
result = ""
for i in setcha:
    if result == "":
        result = result + "(" + str(i) + "**" + str(boluvchilar.count(i)) + ")"
    else:
        result = result + "*" + "(" + str(i) + "**" + str(boluvchilar.count(i)) + ")"


print(diapazon, " = ", result)
# result = str(boluvchilar[0])

# for i in boluvchilar[1:]:
#     result += "*" + str(i)

# print(diapazon, " = ", result)
