# class Employee:
#     emp_soni = 0
#     raise_amount = 1.2

#     def __init__(self, ism, fam, salary, married: bool):
#         self.ism = ism
#         self.fam = fam
#         self.email = ism + fam + "@gmail.com"
#         self.salary = salary
#         self.married = married

#         Employee.emp_soni += 1

#     def __str__(self):
#         return self.ism

#     def raise_salary(self):
#         self.salary = self.salary * self.raise_amount


# emp1 = Employee("Ben", "Parker", 400, True)
# emp2 = Employee("Sam", "Parker", 500, True)

# emp1.raise_amount = 1.3

# print(emp1.salary)
# Employee.raise_salary(emp2)
# emp2.raise_salary()
# print(emp1.salary)
# print(emp2.salary)


# print(Employee.emp_soni)

# print(emp2)


# classmethods, staticmethods
from datetime import date


class Employee:
    emp_soni = 0
    raise_amount = 1.2

    def __init__(self, ism, fam, salary, married: bool):
        self.ism = ism
        self.fam = fam
        self.email = ism + fam + "@gmail.com"
        self.salary = salary
        self.married = married

        Employee.emp_soni += 1

    def __str__(self):
        return self.ism

    # regular method
    def raise_salary(self):
        self.salary = self.salary * self.raise_amount

    @classmethod
    def ornatish_raise_amount(cls, miqdor):
        cls.raise_amount = miqdor

    @staticmethod
    def is_dam(kun: date):
        if kun.weekday() == 6:
            return True
        return False
        # return bool(kun.weekday() % 6)


emp1 = Employee("Ben", "Parker", 400, True)
emp2 = Employee("Sam", "Parker", 500, True)


print(Employee.is_dam(date(2023, 11, 12)))
print(emp1.is_dam(date(2007, 11, 27)))
# print(emp1.salary)
# print(emp2.salary)

# Employee.ornatish_raise_amount(1.7)
# emp1.raise_salary()
# emp2.raise_salary()
# print(emp1.salary)
# print(emp2.salary)
