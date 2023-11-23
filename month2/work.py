def rgb(r, g, b):
    if r < 0:
        red = "00"
    elif r > 255:
        red = "ff"
    elif len(str(hex(r))) == 3:
        red = "0" + str(hex(r))[-1]
    else:
        red = str(hex(r))[2:]

    if g < 0:
        green = "00"
    elif g > 255:
        green = "ff"
    elif len(str(hex(g))) == 3:
        green = "0" + str(hex(g))[-1]
    else:
        green = str(hex(g))[2:]

    if b < 0:
        blue = "00"
    elif b > 255:
        blue = "ff"
    elif len(str(hex(b))) == 3:
        blue = "0" + str(hex(b))[-1]
    else:
        blue = str(hex(b))[2:]
    Red = ""
    Green = ""
    Blue = ""

    for i in red:
        if i.isalpha():
            Red += i.upper()
        else:
            Red += i

    for i in green:
        if i.isalpha():
            Green += i.upper()
        else:
            Green += i

    for i in blue:
        if i.isalpha():
            Blue += i.upper()
        else:
            Blue += i

    return Red + Green + Blue
