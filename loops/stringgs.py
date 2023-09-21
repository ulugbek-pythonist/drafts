# print("A" > "a")
# print("Aziz" > "Aziza")
# ord va chr


# print(ord("?"))
# print(chr(128123))

# is_easy = True

# print(is_easy)
# is_easy = int(is_easy)
# print(is_easy)  # 0 = False  1 = True
# print(float(False))

# a = 10
# a //= 3  # a = a % 3  --> 1
# print(a)

# print(-113 // 10)

# a = str()
# print(type(a))
# print(len(a))
# print(matn)
# print(my_name)

# print("Bu e\b\b\b backslash")

# print("ndiwns \rdiwmd isjdiqw sqdwom \n isjoi")

# print(first_name[1])  # z
# print(first_name[-1])  # k

# print(first_name[4:])  # bek
# print(it[:])  # Python
# print(it[:2])  # Py

# print(my_name[::-1]) #teskarisi


# print("Axis academy"[::3])
# print("hello"[-3:])

# print(f"it: {it}")
# print(f"changed: {it.upper()}")

# print(f"it: {it}")
# print(f"changed: {it.lower()}")

# print(my_name.upper().isupper())  # True
# print(my_name)
# print(my_name.islower())  # False


job = "   Python developer    "

first_name = "Azizbek nimadir"
my_name = "Ulug'bek"
it = "Python"

# print(it.replace("P", "J"))
# # print(it)
# print(job.strip())
# print(job)
# job = job.strip()
# matn = 'Erkin Vohidovning "O\'zbegim" she\'ri "G\'uncha" jurnalida bosildi.'
# print(job.split())
# abc = ["a", "b", "c"]
# print(it.join(abc))


# x = int(input())
# y = int(input())

# print("Sizning joylashuvingiz ({1}:{0})".format(x, y))
a, b = list(map(int, input("a va b ni kiriting: ").split()))
if a > b:
    print("A katta")
elif a == b:
    print("Ular teng")
else:
    print("B katta")
