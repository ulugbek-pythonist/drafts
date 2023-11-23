from abc import ABC, abstractmethod


class A:
    def hello(self):
        print("A class")


class C(A):
    def hello(self):
        print("C class")


class B(A):
    def hello(self):
        print("B class")


class D(C, B):
    pass


d = D()

print(D.__mro__)
d.hello()


class Card(ABC):
    @abstractmethod
    def pay(self, amount):
        print(f"{amount} paid by {self.__class__.__name__}")


class Uzcard(Card):
    def pay(self, amount):
        return super().pay(amount)


class Humo(Card):
    def pay(self, amount):
        return super().pay(amount)


my_card = Uzcard()
my_card.pay(30)

his_card = Humo()
his_card.pay(30)
