import time
from random import randint as son


n = int(input("Nechta savol xohlaysiz: "))
scores = 0  # 10 ball
amount = 0  # to'g'ri javoblar soni
holat = {}

start = time.time()

for i in range(1, n + 1):
    print("-------------------------------------------------")
    savol = f"{son(70,100)} - {son(10,30)} + {son(20,40)}"
    print(f"🏁{i}-savol\n{savol} = ?")
    javob = eval(savol)
    fjavob = int(input("javob:➡️  "))
    if fjavob == javob:
        amount += 1
        scores += 10
        holat[javob] = str(fjavob) + "✅"
    else:
        holat[javob] = str(fjavob) + "❌"

stop = time.time()
vaqt = stop - start
print("---------------------------------------------")
for key, val in holat.items():
    print(f"javob: {key} --> senig javobing: {val}")
print(
    f"\n\nNatija:{n} tadan {amount} ta to'g'ri\n📝 {scores} ball\n⏰ {round(vaqt,2)} soniya\n📈 {round(amount*100/n)} %"
)
