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


for i in range(101):
    print(i, " ", is_tub(i))
