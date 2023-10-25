# from openpyxl import Workbook, load_workbook
# from random import randint

# filename = "seshanba/new/grades.xlsx"
# # wb = load_workbook(filename)

# # # ws = wb.active
# # # ws["A1"].value = "Names"
# # # print(ws["A2"].value)

# # # wb.save(filename)

# # wb.create_sheet("days")

# # print(wb.sheetnames)

# new_wb = Workbook()
# ws = new_wb.active
# ws.title = "Database"

# for i in range(1, 10):
#     ws[f"A{i}"] = randint(10, 30)

# new_wb.save("archive/sam.xlsx")

# soz = input("So'zni kiriting: ")
# result = ""

# for i in soz:
#     if i.lower() == "a":
#         result += "i"
#     elif i.lower() == "i":
#         result += "a"
#     else:
#         result += i

# print(result)


# dictionaries  ---> lug'atlar

# a = {}
# print(a)
# print(type(a))

# {kalit:qiymat,key:value,...}

# sozlar = {"suv": "water", "bulut": "cloud"}

# accessing --> elementlariga murojaat qilish

# print(sozlar["bulut"])  # "cloud"

# print(sozlar["ovqat"])  # key error

# print(sozlar.get("ovqat"))  # None

# print(sozlar.get("ovqat", "Hech narsa topilmadi"))  # "Hech narsa topilmadi"


# # elementlarni(kalit-qiymat juftliklarini) o'zgartirish
# sozlar = {"suv": "water", "bulut": "cloud"}

# sozlar["bulut"] = "rain"

# print(sozlar)  #  {"suv":"water","bulut":"rain"}

# # elementlar(kalit-qiymat juftliklar) qo'shish
# sozlar = {"suv": "water", "bulut": "cloud"}

# sozlar["ovqat"] = "food"

# print(sozlar)  #  {"suv":"water","bulut":"cloud","ovqat":"food"}

# # elementlar(kalit-qiymat juftliklar) o'chirish
# sozlar = {"suv": "water", "bulut": "cloud", "ovqat": "food"}

# del sozlar["ovqat"]

# print(sozlar)  # {"suv":"water","bulut":"cloud"}
