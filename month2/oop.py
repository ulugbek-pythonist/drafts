# OOP

# Object Oriented Programming

# Obyektga yo'naltirilgan dasturlash

# Hayvonlar     Baliq, Kiyik, Qo'y

# Sinflarni hosil qilish

from abc import abstractmethod
from random import randint


class Animal:
    def __init__(self, name: str, age: int, turi: str):
        self.name = name
        self.age = age
        self.turi = turi

    def __str__(self):
        return self.name

    def info(self):
        return f"{self.name}lar {self.turi} hisoblanadi, o'rtacha {self.age} yil umr ko'radi."


a = Animal("Baliq", 40, "Suv hayvoni")  # namuna
b = Animal("Kiyik", 20, "O'rmon hayvoni")  # namuna

# a.name = "Akula"
# a.age = 30

# print(a.info())
# print(Animal.info(b))

# print(b.info())


class Employee:
    total = 0
    oshirish = 1.2

    def __init__(self, first_name, last_name, salary) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + last_name + str(randint(20, 90)) + "@gmail.com"
        self.salary = salary
        Employee.total += 1

    @abstractmethod
    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    def raise_salary(self):
        self.salary = self.salary * self.oshirish


xodim1 = Employee("Azizbek", "Zokirjonov", 300)
xodim2 = Employee("Samandar", "Erkinov", 500)
xodim3 = Employee("Bobur", "Erkinov", 1000)

# print(xodim1.salary)
# # Employee.raise_salary(xodim1)
# xodim1.oshirish = 1.5
# xodim1.raise_salary()
# print(xodim1.salary)

# print(xodim1.email)

# print(f"{xodim1.first_name} {xodim1.last_name}")
# print("{} {}".format(xodim1.first_name,xodim1.last_name))

# print(xodim1.fullname())
# print(xodim2.fullname())
# print(Employee.fullname(xodim1))
# print(Employee.total)


class Developer(Employee):
    def __init__(self, first_name, last_name, salary, prog_lang):
        super().__init__(first_name, last_name, salary)
        self.prog_lang = prog_lang


dev1 = Developer("Sam", "Parker", 60000, "Kotlin")

print(dev1.salary)
dev1.raise_salary()
print(dev1.salary)

print(dev1.fullname())
