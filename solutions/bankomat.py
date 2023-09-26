text1 = "-- Balans (1)\n\
-- Valyuta ayirboshlash (2)\n\
-- SMS xabar ulash (3)\n\
-- O'tkazmalar (4)\n\
\n\
Xizmat turini tanlang(1/2/3/4): "
text2 = "-- Valyuta ayirboshlash (2)\n\
-- so'mni dollarga (1)\n\
-- dollarni  so'mga (2)\n\
\n\
Tanlang(1/2): "
balance = "--- Balans\n\
Hisobingizda 2000000 so'm"
inform = input(text1)

if inform == "1":
    print(balance)
elif inform == "2":
    inform2 = input()
