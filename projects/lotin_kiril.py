kiril = "абдефгҳижклмонпқрстувхйз"
kiril1 = "ў"
kiril2 = "ғ"
kiril3 = "ш"
kiril4 = "ч"

lotin = "abdefghijklmonpqrstuvxyz"
lotin1 = "o'"
lotin2 = "g'"
lotin3 = "sh"
lotin4 = "ch"

matn = input("Matn: ")
natija = ""

for i in matn:
    if i.islower():
        indeks = lotin.index(i)
        natija += kiril[indeks]
    elif i.isupper():
        indeks = lotin.upper().index(i)
        natija += kiril.upper()[indeks]
    elif i.isdigit():
        natija += i
    else:
        natija += i


print(natija)
