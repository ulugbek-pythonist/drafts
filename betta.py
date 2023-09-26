# number = 23.37483
# print("{:.3f}".format(number))
# print("%.2f" % number)
# print("%d" % -2.3)
# a = 3

# shart1 = True
# shart2 = True
# shart3 = True
# shart4 = True

# if shart1:
#     if shart2:
#         print("shart1 va shart2 bajariladi")
#     elif shart3:
#         print("shart1 va shart3 bajariladi")
#     else:
#         print("shart1 bajariladi")
# elif shart4:
#     print("shart4 bajariladi")
# else:
#     print("Hech bir shart bajarilmaydi")
# from math import e


# a = e
# print(f""" {e} """)


# my_list = ["and", "for", "loop", "again", "break"]
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)

# a = {"key1", "key2", "key3", "key4"}
# b = "value"

# newone = {}.fromkeys(a, b)
# print(newone)


# class Programming:
#     def __init__(self, name) -> None:
#         self.name = name


# class Java(Programming):
#     pass


# c = Programming("Python")

# print(issubclass(Java, Programming))
# print(isinstance(c, Programming))

# # issubclass(A,B)   checks if A is subclass of B
# # it  means A is child class B is parent class


my_func = lambda a: a**2


# a, b, c = list(map(float, input().split()))
# print(type(a))
# print(type(b))
# print(type(c))

# a = [1, 2, 3, 4, 5]
# b = ["Facebook", "google", "amazon"]
# print(type(zip(a, b)))
# print(dict(zip(a, b)))


# def filtrlayman(a):
#     letters = ["a", "b"]
#     if a in letters:
#         return True
#     else:
#         return False


# p = "F a a c e b o o k".split(" ")
# print(p)
# filtered = filter(filtrlayman, p)
# print(p)
# print(list(filtered))

# mapped = tuple(map(my_func, a))
# print(mapped)

# word = "hello"
# sliced = slice(2)
# print(word[sliced])


def fun_generator():
    yield "Hello world!!"
    yield "Geeksforgeeks"


obj = fun_generator()

# print(type(obj))

# print(next(obj))
# print("end")
# print(next(obj))

# for i in obj:
#     print(i, end=" ")


# def inf_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1
#         if num == 1000:
#             break


# for i in inf_sequence():
#     print(i, end=" ")
