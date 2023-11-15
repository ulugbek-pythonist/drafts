class Circle:
    def __init__(self, radius) -> None:
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, R):
        if R <= 0:
            raise ValueError("radius can not be negative")
        else:
            self.__radius = R

    @radius.deleter
    def radius(self):
        del self.__radius
        self.__radius = None

    def __str__(self):
        return self.radius


print(Circle.__new__(Circle))
