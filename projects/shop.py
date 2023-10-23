import time


chiziq = "--------------------------------------"

products_kg = {
    "olma": 5000,
    "un": 6000,
    "shakar": 4500,
    "kartoshka": 3500,
    "piyoz": 7000,
    "sabzi": 2700,
    "sarimsoq piyoz": 10000,
    "guruch": 15000,
    "shokolad": 20000,
}

products_ta = {
    "suv 0.5 l": 2000,
    "suv 1 l": 3000,
    "sharbat": 8000,
    "qatiq": 7000,
    "non": 2800,
    "kofe 100 g": 20000,
    "kofe 200 g": 30000,
    "sut 1 l": 11000,
}

aravacha = {}
narxlar = {}

time.sleep(1)
c = 1
for key, value in products_kg.items():
    print(f"{c}. 1 kg {key} --- {value} so'm")
    c += 1
print(chiziq)
time.sleep(1)
for key, value in products_ta.items():
    print(f"{c}. 1 ta {key} --- {value} so'm")
    c += 1
print(chiziq)

while True:
    mahsulot = input("Mahsulot tanlang(chiqish u-n quit): ")
    if mahsulot.lower() == "quit":
        break
    miqdor = input("Nechta yoki necha kg olasiz (chiqish u-n quit): ")
    if miqdor.lower() == "quit":
        break

    mahsulot = int(mahsulot)
    miqdor = float(miqdor)
    if 0 < mahsulot < 10:
        kalit = list(products_kg.keys())[mahsulot - 1]
        aravacha[kalit] = miqdor
        narxlar[kalit] = products_kg[kalit] * miqdor
    elif 10 <= mahsulot < 18:
        kalit = list(products_ta.keys())[mahsulot - 10]
        aravacha[kalit] = miqdor
        narxlar[kalit] = products_ta[kalit] * miqdor

    time.sleep(0.5)
    c = 1
    for key, value in products_kg.items():
        print(f"{c}. 1 kg {key} --- {value} so'm")
        c += 1
    print(chiziq)
    time.sleep(0.5)
    for key, value in products_ta.items():
        print(f"{c}. 1 ta {key} --- {value} so'm")
        c += 1
    print(chiziq)
total = 0
for kalit, qiymat in aravacha.items():
    print(f"{kalit} {qiymat} (kg/ta) ---> {narxlar[kalit]} so'm")
    total += narxlar[kalit]

print(f"Jami: {total} so'm")
