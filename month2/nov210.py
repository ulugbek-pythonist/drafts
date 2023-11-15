def bol(n):
    s = []
    for i in range(2, n + 1):
        if i > n:
            break

        while n % i == 0:
            s.append(i)
            n = n // i

    return s


def EKUB(a, b):
    num = 1
    bol_a = bol(a)
    bol_b = bol(b)
    nums = set(bol_a).intersection(set(bol_b))

    for i in nums:
        num *= i ** min(bol_a.count(i), bol_b.count(i))

    return num


print(EKUB(246, 36))
