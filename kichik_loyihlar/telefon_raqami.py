# phone = input("Enter phone number (901234567): ")


def telefon(phone):
    phone = str(phone)
    while (
        (not phone.isdigit())
        or (not len(phone) == 9)
        or (phone[:2] not in ["90", "91", "93", "94", "95", "97", "99"])
    ):
        phone = input("Enter phone number (901234567): ")

    return "+998 ({}{}) {}{}{}-{}{}-{}{}".format(*phone)


phone_number = telefon(932002020)
print(phone_number)
