class Example:
    def __init__(self, question) -> None:
        self.question = question

    def __del__(self):
        print("deleted")

    def __test__(self):
        print("test")

    def __add__(self, value):
        print("Almost added")
        self.question = self.question + value

    def __str__(self) -> str:
        return self.question


a = Example("How are you?")
a.__add__(" Okay?")
print(a)
print(dir(Example))

print(Example.__getattribute__(a, "question"))
