def telefon(phone):
    phone = str(phone)
    while (
        (not phone.isdigit())
        or (not len(phone) == 9)
        or (
            phone[:2]
            not in ["50", "90", "91", "93", "98", "88", "33", "94", "95", "97", "99"]
        )
    ):
        phone = input("Telefon raqamini kiriting: +998 ")

    return "+998 ({}{}) {}{}{}-{}{}-{}{}".format(*phone)


def karta_raqam(karta):
    karta = str(karta)
    while (
        (not karta.isdigit())
        or (karta[:4] not in ["8600", "9860"])
        or (len(karta) != 16)
    ):
        karta = input(
            "--* 8600 yoki 9860 bilan boshlanishi\n\
--* 16 ta raqam bo'lishi kerak\n\
Karta raqamini kiriting: "
        )

    return karta


def bankomat():
    text1 = "------------------------------------------------------------------\n\
    \n-- Balans (1)\n\
-- Valyuta ayirboshlash (2)\n\
-- SMS xabar ulash (3)\n\
-- O'tkazmalar (4)\n\
    \n\
    Xizmat turini tanlang(1/2/3/4): "
    text2 = "\n\n-------------------------------------------------------------------\n\
    -- Valyuta ayirboshlash (2)\n\
    -- so'mni dollarga (1)\n\
    -- dollarni  so'mga (2)\n\
    \n\
    -- ortga (3)\n\
    \n\
    Tanlang(1/2): "
    text3 = "\n\n--------------------------------------------------------------------\n\
    (SMS xabar ulash)\n\
    \n\
    --* 9ta raqam kiritiladi\n\
    --* 33,50,88,90,91,93,94,95,97,98,99 shularning biri bilan boshlanishi kerak\n\
    \n\
    -- ortga(0)\n\n\
    Telefon raqamini kiriting (ortga qaytish uchun 0 ni kiriting): +998  "

    text4 = "\n\n--------------------------------------------------------------------\n\
    (O'tkazmalar)\n\
    \n\
    --* 8600 yoki 9860 bilan boshlanishi\n\
    --* 16 ta raqam bo'lishi kerak\n\
    \n\
    -- ortga(0)\n\n\
    Karta raqamini kiriting(ortga qaytish uchun 0 ni kiriting): "

    valyuta1 = "-- so'mni dollarga\n\
    \n\
    (1 so'm = 0.000082 $)\n\
    \n\
    Qiymat kiriting: "
    valyuta2 = "-- dollarni  so'mga\n\
    \n\
    (1 $ = 12168 so'm)\n\
    \n\
    Qiymat kiriting:"

    password = "abC@97py"
    tasdiqlaysizmi = "\nTasdiqlaysizmi (ha/yo'q):\n\
        -- ha (1)\n\
        -- yo'q (2)\n\
        --> "
    lack = "Balansda yetarli mablag' yo'q"
    money = 2000000
    inform = input(text1)

    if inform == "1":
        print(
            f"\n\n--- Balans\n\
    Hisobingizda {money} so'm bor."
        )
        option = input(
            "-----------------------------------------------------------------------\n\
        Bosh menyuga qaytasizmi?\n\
        -- ha (1)\n\
        -- yo'q (2)\n\n\
        Tanlang: "
        )
        while option not in ("1", "2"):
            option = input(
                "-------------------------------------------------------------------------\n\
            Bosh menyuga qaytasizmi?\n\
            -- ha (1)\n\
            -- yo'q (2)\n\n\
            Tanlang: "
            )

        if option == "1":
            bankomat()
        elif option == "2":
            print("Xayr, salomat bo'ling!")
    elif inform == "2":
        inform2 = input(text2)
        if inform2 == "1":
            option1 = int(input(valyuta1))
            if option1 > money:
                print(lack)
                option = input(
                    "-----------------------------------------------------------------------\n\
        Bosh menyuga qaytasizmi?\n\
        -- ha (1)\n\
        -- yo'q (2)\n\n\
        Tanlang: "
                )
                while option not in ("1", "2"):
                    option = input(
                        "-------------------------------------------------------------------------\n\
                    Bosh menyuga qaytasizmi?\n\
                    -- ha (1)\n\
                    -- yo'q (2)\n\n\
                    Tanlang: "
                    )

                if option == "1":
                    bankomat()
                elif option == "2":
                    print("Xayr, salomat bo'ling!")
            else:
                print(f"{option1} so'm --> {option1*0.000082} $")
                yesno = input(tasdiqlaysizmi)
                if yesno == "1":
                    print(
                        f"{option1*0.000082} $ yechib olindi, marhamat, pullarni oling"
                    )
                elif yesno == "2":
                    print("Operatsiya bekor qilindi.")
                    option = input(
                        "-----------------------------------------------------------------------\n\
        Bosh menyuga qaytasizmi?\n\
        -- ha (1)\n\
        -- yo'q (2)\n\n\
        Tanlang: "
                    )
                    while option not in ("1", "2"):
                        option = input(
                            "-------------------------------------------------------------------------\n\
                        Bosh menyuga qaytasizmi?\n\
                        -- ha (1)\n\
                        -- yo'q (2)\n\n\
                        Tanlang: "
                        )

                    if option == "1":
                        bankomat()
                    elif option == "2":
                        print("Xayr, salomat bo'ling!")
        elif inform2 == "2":
            option2 = int(input(valyuta2))
            if (option2 * 12168) < money:
                print(f"{option2} $ --> {option2*12168} so'm")
                yesno = input(tasdiqlaysizmi)
                if yesno == "1":
                    print(
                        f"{option2*12168} so'm yechib olindi, marhamat, pullarni oling"
                    )
                elif yesno == "2":
                    print("Operatsiya bekor qilindi.")
                    option = input(
                        "-----------------------------------------------------------------------\n\
        Bosh menyuga qaytasizmi?\n\
        -- ha (1)\n\
        -- yo'q (2)\n\n\
        Tanlang: "
                    )
                    while option not in ("1", "2"):
                        option = input(
                            "-------------------------------------------------------------------------\n\
                        Bosh menyuga qaytasizmi?\n\
                        -- ha (1)\n\
                        -- yo'q (2)\n\n\
                        Tanlang: "
                        )

                    if option == "1":
                        bankomat()
                    elif option == "2":
                        print("Xayr, salomat bo'ling!")
            else:
                print(lack)
                option = input(
                    "-----------------------------------------------------------------------\n\
        Bosh menyuga qaytasizmi?\n\
        -- ha (1)\n\
        -- yo'q (2)\n\n\
        Tanlang: "
                )
                while option not in ("1", "2"):
                    option = input(
                        "-------------------------------------------------------------------------\n\
                    Bosh menyuga qaytasizmi?\n\
                    -- ha (1)\n\
                    -- yo'q (2)\n\n\
                    Tanlang: "
                    )

                if option == "1":
                    bankomat()
                elif option == "2":
                    print("Xayr, salomat bo'ling!")
        elif inform2 == "3":
            bankomat()
    elif inform == "3":
        phone = input(text3)
        if phone == "0":
            bankomat()
        else:
            phone = telefon(phone)
            parol = input(
                f"\n\n---------------------------------------------------------------\n\
        {phone} raqamiga sms orqali parol yuborildi\n\
        Parolni kiriting: "
            )
            a = 0
            while parol != password:
                a += 1
                if a == 3:
                    break
                parol = input(f"Parolni kiriting ({3-a} ta urinish qoldi): ")

            if a == 3:
                print("Karta ulanmadi.")
                option = input(
                    "-----------------------------------------------------------------------\n\
        Bosh menyuga qaytasizmi?\n\
        -- ha (1)\n\
        -- yo'q (2)\n\n\
        Tanlang: "
                )
                while option not in ("1", "2"):
                    option = input(
                        "-------------------------------------------------------------------------\n\
                    Bosh menyuga qaytasizmi?\n\
                    -- ha (1)\n\
                    -- yo'q (2)\n\n\
                    Tanlang: "
                    )

                if option == "1":
                    bankomat()
                elif option == "2":
                    print("Xayr, salomat bo'ling!")
            else:
                print(f"Karta {phone} raqamiga muvaffaqiyatli ulandi")
                option = input(
                    "-----------------------------------------------------------------------\n\
        Bosh menyuga qaytasizmi?\n\
        -- ha (1)\n\
        -- yo'q (2)\n\n\
        Tanlang: "
                )
                while option not in ("1", "2"):
                    option = input(
                        "-------------------------------------------------------------------------\n\
                    Bosh menyuga qaytasizmi?\n\
                    -- ha (1)\n\
                    -- yo'q (2)\n\n\
                    Tanlang: "
                    )

                if option == "1":
                    bankomat()
                elif option == "2":
                    print("Xayr, salomat bo'ling!")
    elif inform == "4":
        karta = input(text4)
        if karta == "0":
            bankomat()
        else:
            karta = karta_raqam(karta)
            amount = input(
                "\n\n---------------------------------------------------------------\n\
        Qancha o'tkazamiz: "
            )
            amount = int(amount)
            if amount > money:
                print(lack)
                option = input(
                    "-----------------------------------------------------------------------\n\
        Bosh menyuga qaytasizmi?\n\
        -- ha (1)\n\
        -- yo'q (2)\n\n\
        Tanlang: "
                )
                while option not in ("1", "2"):
                    option = input(
                        "-------------------------------------------------------------------------\n\
                    Bosh menyuga qaytasizmi?\n\
                    -- ha (1)\n\
                    -- yo'q (2)\n\n\
                    Tanlang: "
                    )

                if option == "1":
                    bankomat()
                elif option == "2":
                    print("Xayr, salomat bo'ling!")
            else:
                print(f"{amount} so'm o'tkaziladi")
                yesno = input(tasdiqlaysizmi)
                if yesno == "1":
                    print(f"{amount} so'm o'tkazildi")
                elif yesno == "2":
                    print("Operatsiya bekor qilindi.")
                    option = input(
                        "-----------------------------------------------------------------------\n\
        Bosh menyuga qaytasizmi?\n\
        -- ha (1)\n\
        -- yo'q (2)\n\n\
        Tanlang: "
                    )
                    while option not in ("1", "2"):
                        option = input(
                            "-------------------------------------------------------------------------\n\
                        Bosh menyuga qaytasizmi?\n\
                        -- ha (1)\n\
                        -- yo'q (2)\n\n\
                        Tanlang: "
                        )

                    if option == "1":
                        bankomat()
                    elif option == "2":
                        print("Xayr, salomat bo'ling!")
    else:
        bankomat()


bankomat()
