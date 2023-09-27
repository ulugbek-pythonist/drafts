# phone = input("Enter phone number (901234567): ")


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


phone_number = telefon(932002020)
print(phone_number)


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
