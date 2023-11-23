# def my_deco(func):
#     def implement():
#         print("some text")
#         return func()

#     return implement


# @my_deco
# def my_func():
#     return "hello"


# print(my_func())

# from functools import reduce

# a = [2, 4, 5, 6]

# result = reduce(lambda x, y: x * y, a)
# result = filter(lambda x: x < 5, a)

# for i in result:
#     print(i)


# def myfunc():
#     global x
#     x = 300


# myfunc()
# print(x)


class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    def __add__(self, other: "Employee"):
        return self.salary + other.salary

    def __mul__(self, other: "Employee"):
        return self.salary * other.salary

    def __sub__(self, other: "Employee"):
        return abs(self.salary - other.salary)

    def __truediv__(self, other: "Employee"):
        return round(self.salary / other.salary, 2)

    def __mymethod__(self, other: "Employee"):
        return round((self.salary + other.salary) ** 0.5, 3)


# emp1 = Employee("Bobur", 300)
# emp2 = Employee("Tohir", 500)
# # a = 5
# print(emp1 + emp2)
# print(emp1 * emp2)
# print(emp1 - emp2)
# print(emp2 / emp1)
# print(emp1.__mymethod__(emp2))
# # print(a.__add__(10))
# emp1.__setattr__("school", "maktab 29")
# print(emp1.school)
# Employee.__delattr__(emp1, "name")
# print(emp1.name)

