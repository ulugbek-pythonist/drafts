text1 = """----------------------------------------
        Bankomat

1. Balans
2. Hisobni to'ldirish
3. SMS xabar ulash
4. Valyuta ayirboshlash
5. Chiqish

    Xizmat turini tanlang(1/2/3/4/5): """

tel_text = """-------------------------------------------
        SMS xabar ulash

Telefon raqamini kiriting:  + 998 """

val_text = """--------------------------------------------
            Valyuta ayirboshlash

        So'mni dollarga

    ( 1 so'm = 0.000081 $ )

Necha so'm ayirboshlaysiz: """

balans = 4000000
parol = "123"
xayr = "Xayr, salomat bo'ling!"
chiziq = "-------------------------------------------"
tasdiqlaysizmi = """----------------------------------
-- ha (1)
-- yo'q (2)

Tasdiqlaysizmi: """

tanlov1 = input(text1)

if tanlov1 == "1":
    print(chiziq)
    print(f"Hisobingizda {balans} so'm mavjud")
    print(xayr)
elif tanlov1 == "2":
    print(chiziq)
    print(f"Hisobingizda {balans} so'm mavjud")
    pul = input("Hisobingizni qanchaga to'ldirasiz: ")
    print(chiziq)
    print(f"Hisobingiz {pul} so'mga to'ldiriladi")
    is_ok = input(tasdiqlaysizmi)
    if is_ok == "1":
        print(chiziq)
        print("Operatsiya muvaffaqiyatli yakunlandi")
        print("Joriy hisob: ", balans + int(pul), " so'm")
        print(xayr)
    elif is_ok == "2":
        print(chiziq)
        print("Operatsiya bekor qilindi")
        print(xayr)
elif tanlov1 == "3":
    tel = input(tel_text)

    while not tel.isdigit():
        tel = input("Qayta kiriting: + 998 ")

    print(chiziq)
    print(f"Parol + 998 {tel} raqamiga yuborildi")
    kod = input("Parolni kiriting: ")
    imkoniyat = 3

    while kod != parol:
        imkoniyat -= 1
        if imkoniyat == 0:
            break

        kod = input(f"Parolni kiriting({imkoniyat} ta urunish qoldi): ")

    if imkoniyat == 0:
        print("Parol noto'g'ri kiritildi, sms xabar xizmati ulanmadi")
    else:
        print("SMS xabar xizmati muvaffaqiyatli ulandi")
        print(xayr)
elif tanlov1 == "4":
    money = int(input(val_text))
    dollar = money * 0.000081
    if money > balans:
        print(chiziq)
        print("Balansda mablag' yetarli emas")
        print(xayr)
    elif money <= balans:
        print(chiziq)
        print(f"{money} so'm --> {dollar} $ ga almashtiriladi")
        hami = input(tasdiqlaysizmi)

        if hami == "1":
            print(chiziq)
            print(f"Marhamat {dollar} $")
            print(f"Balansda {balans - money} so'm qoldi")
            print(xayr)
        elif hami == "2":
            print("Operatsiya bekor qilindi")
            print(xayr)
        else:
            print("Xatolik yuz berdi, dasturni qayta ishga tushiring")
            print(xayr)
elif tanlov1 == "5":
    print(xayr)
else:
    print("Xatolik yuz berdi, dasturni qayta ishga tushiring")

# print("XAYR!")
