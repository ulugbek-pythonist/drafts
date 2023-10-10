# bomba

import time

vaqt = int(input("Vaqtni sekundlarda kiriting: "))


for i in range(vaqt):
    soat = int(vaqt / 3600)
    minut = int((vaqt - 3600 * soat) / 60)
    sekund = vaqt % 60
    print(f"{soat:02}:{minut:02}:{sekund:02}")
    time.sleep(1)
    vaqt = vaqt - 1

print("Boom!")
