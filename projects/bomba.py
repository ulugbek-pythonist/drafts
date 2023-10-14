import time

print("------------Bomba----------")

vaqt = input("Vaqtni sekundlarda kiriting: ")

while not vaqt.isdigit():
    vaqt = input("Vaqtni sekundlarda kiriting: ")

vaqt = int(vaqt)

for a in range(vaqt):
    soat = vaqt // 3600
    daqiqa = (vaqt - soat * 3600) // 60
    soniya = vaqt % 60
    print(f"{soat:02}:{daqiqa:02}:{soniya:02}")
    vaqt -= 1
    time.sleep(1)

print("boom!")
