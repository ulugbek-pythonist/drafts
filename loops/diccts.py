# Dictionaries in python
# int,str,float,bool --> primitive types
# collection types dictionary
# "apple" -- > "olma"


#  nomi = { key:value, key2:value }
# collection types

# print(my_dict)
# Hosil qilish {} bilan yoki dict()

# lugat = {}
# print(type(lugat))
# print(lugat)

# accessing items --> elementlarga murojaat qilish

# my_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# my_dictionary[key] = value # xatolik berishi mumkin
# my_dictionary.get(key) = value # xatolik bermaydi

# print(my_dict.get(6, 100))
# my_dict = {"my_num": 12, "age": 22}

# print(f"My number is {my_dict['my_num']} and I'm {my_dict.get('age',20)}")

# print(my_dict["my_name"])

# print(my_dict.get(10))

# print(None == False)
# None -- > Nonetype
# False --> bool

# adding items

# print(lugat)
# lugat["my_num"] = "Python developer"
# print(lugat)

# print(kalit)
# print(qiymat)

# kalit qiymat kalit lugatimizda bo'lsa unga mos qiymatni chiqarsin
# agar bo'lmasa kiritilgan juftlikni qo'shib qo'ysin


# # masala foydalanuvchi key va value ni kiritadi --> value agar bo'lmasa
# # o'zimiz qo'shishimiz kerak key value

# # my_num "jsdni",  "job"  --> 'pilot'


my_dict = {"my_num": 12, "my_name": "Ulug'bek", 10: 22}
kalit, qiymat = input("kalit va qiymatni kiriting: ").split()

if my_dict.get(kalit):
    print(my_dict[kalit])
else:
    my_dict[kalit] = qiymat

print(my_dict)


# print(ord("@"))
# print(chr(1201))

# lugat = {"key": "value", "keycha": "valuecha"}

# print(lugat)
# if "keyb" in lugat.keys():
#     del lugat["keyb"]
# print(lugat)
# x = ('key1', 'key2', 'key3')
# y = 0

# thisdict = dict.fromkeys(x, y)


# print(thisdict)
