# quiz game

from random import randint as num

n = int(input("Nechta savol istaysan: "))
scores = 0
amount = 0

for i in range(1,n + 1):
    savol = f"{num(50,70)} - {num(10,30)} + {num(2,12)}"
    print(f"{i}-savol.\n{savol} = ?")
    javob = eval(savol)
    fjavob = int(input("javob: "))
    if javob == fjavob:
        scores += 10
        amount += 1

print(f"Natija: {amount}/{n}\n{scores} points")

