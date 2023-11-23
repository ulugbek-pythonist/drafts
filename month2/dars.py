# method resolution order MRO (metodni joriy qilish tartibi)


# parent class


# class A:
#     secret = "2010"

#     def __init__(self, ip) -> None:
#         self.ip = ip

#     def hello(self):
#         print("A class")


# # child class (subclass)
# class B(A):
#     def __init__(self, ip) -> None:
#         super().__init__(ip)

#     def func(self):
#         return super().hello()

#     def print_secret(self):
#         print(super().secret)

#     def hello(self):
#         print("B class")


# b = B("2827387382")

# b.func()
# b.print_secret()


# class C(A):
#     def hello(self):
#         print("C class")


# class D(C, B):
#     pass


# d = D("1222222")
# print(D.__mro__)
# d.hello()

# 4 pillars of OOP: OOP ning 4 ustuni

# inheritance (meros olish)

# encapsulation (inkapsulyatsiya)

# poly-morph-ism (many-form-ism) (ko'p formalilik (jihatlilik))

# abstraction (mavhumlik)


# class Customer:
#     def __init__(self, name, balance, password) -> None:
#         self.name = name  # public member (ommaviy a'zo)
#         self.__balance = balance  # private member  (maxfiy a'zo)
#         self._password = password  # protected member (himoyalangan a'zo)

#     def show_balance(self):
#         return self.__balance

#     def pay(self, amount):
#         if amount > self.__balance:
#             print("Balansda yetarli mablag' yo'q")
#         else:
#             print(f"{amount} $ ketdi")
#             self.__balance -= amount


# class VipCustomer(Customer):
#     pass


# premium = VipCustomer("Samandar", 300)

# print(premium.show_balance())

# customer1 = Customer("David", 130, "uxhx98h3hwe")


# print(customer1.name)

# print(customer1.show_balance())

# customer1.pay(100)
# # customer1.__balance = 100
# # customer1.name = "Azizbek"
# # print(customer1.name)
# print(customer1.show_balance())
# print(customer1._password)

# polymorphism

# print(len("anhor"))  # str
# print(len(["2", 3.5, True]))  # list
# print(len(("2", 3.5, True)))  # tuple
# print(len({"2", 3.5, True}))  # set
# print(len({1: 1, 2: 4}))  # dict


# class Animal:
#     def __init__(self, name) -> None:
#         self.name = name

#     def make_sound(self):
#         pass


# class Dog(Animal):
#     def make_sound(self):
#         print("Wuuf-wuuf!")


# class Cat(Animal):
#     def make_sound(self):
#         print("Meow-meow!")


# class Wolf(Animal):
#     def make_sound(self):
#         print("Auuuuu-auuuuuu!")


# dog = Dog("Bobik")
# cat = Cat("Malla")
# wolf = Wolf("Bo'ri")

# dog.make_sound()
# cat.make_sound()
# wolf.make_sound()

# abstraction (mavhumlik)

from abc import ABC, abstractmethod
import datetime


class Card(ABC):
    @abstractmethod
    def pay(self):
        print(f"pay from {self.__class__.__name__}")


class Uzcard(Card):
    def pay(self):
        return super().pay()


class Humo(Card):
    def pay(self):
        return super().pay()


humo_karta = Humo()
uzkard = Uzcard()

# print(uzkard.__class__.__name__)
humo_karta.pay()
uzkard.pay()

print(datetime.date.today() > datetime.date(2026, 1, 1))
