def massimo_comune_divisore(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return massimo_comune_divisore(b, r)


print(massimo_comune_divisore(126, 147))