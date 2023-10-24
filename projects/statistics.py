import pygal

line = pygal.Bar()

line.title = "Aholi statistika"
line.x_labels = []
n = int(input("How many months do you add: "))
_n = n
while n > 0:
    a = input("Add month for statistics: ")
    line.x_labels.append(a)
    n -= 1

m = int(input("How many countries do you add: "))
while m > 0:
    b = input("Add country: ")
    c = input(f"Enter {_n} population amounts separated with spaces:").split()
    c = list(map(int, c))
    line.add(b, c)
    m -= 1

line.render_in_browser()
