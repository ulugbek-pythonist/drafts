# args and kwargs


def add(*args):
    s = 0
    for i in args:
        s += i

    return s


print(add(1, 2, 3, 4, 5, 6))


def info(*args, **kwargs):
    for i in args:
        print(i, end=" ")

    print()

    for k, v in kwargs.items():
        print(f"({k}:{v})", end=" ")

    print()


info(1, 2, 3, name="bob", age=30)
