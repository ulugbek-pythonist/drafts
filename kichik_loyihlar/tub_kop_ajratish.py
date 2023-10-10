from math import sqrt as ildiz

tub_sonlar = {
    2,
}


def is_tub(son):
    son = int(son)
    if son <= 0:
        return "Natural son kiriting"

    if son in tub_sonlar:
        return True

    diapazon = round(ildiz(son))
    b_soni = 0

    for i in range(1, diapazon + 1):
        if son % i == 0:
            b_soni += 1

    if son == 1 or b_soni > 1:
        return False

    tub_sonlar.add(son)
    return True


# n = int(input("Sonni kiriting: "))
n = 217815905797 * 110917
print(n)
diapazon = n
boluvchilar = []

if is_tub(n):
    print("Bu tub son: ", f"{n} = 1*{n}")
else:
    for i in range(2, diapazon):
        if n < i:
            break
        if not is_tub(i):
            continue
        while n % i == 0:
            boluvchilar.append(str(i))
            n /= i

    print(diapazon, " = ", "*".join(boluvchilar))
    # Pro
    # setcha = set(boluvchilar)
    # result = ""
    # for i in setcha:
    #     if result == "":
    #         result = result + "(" + str(i) + "**" + str(boluvchilar.count(i)) + ")"
    #     else:
    #         result = (
    #             result + "*" + "(" + str(i) + "**" + str(boluvchilar.count(i)) + ")"
    #         )
    # print(diapazon, " = ", result)
