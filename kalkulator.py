def husvet(ev: int):
    if (1583 <= ev) and (ev <= 1699):
        szamol(ev, 22, 2)
        m = 22
        n = 2
    elif ev <= 1799:
        szamol(ev, 23, 3)
        m = 23
        n = 3
    elif ev <= 1899:
        szamol(ev, 23, 4)
        m = 23
        n = 4
    elif ev <= 2099:
        szamol(ev, 24, 5)
        m = 24
        n = 5
    elif ev <= 2199:
        szamol(ev, 24, 6)
        m = 24
        n = 6
    elif ev <= 2299:
        szamol(ev, 25, 0)
        m = 25
        n = 0


def szamol(ev: int, m: int, n: int):
    a = ev % 19
    b = ev % 4
    c = ev % 7

    if (1900 <= ev) and (ev <= 2099):
        d = ((19 * a) + m) % 30
        e = ((2 * b) + (4 * c) + (6 * d) + n) % 7

        if d + e < 10:
            nap = str(d + e + 22)
            print("Március " + nap + ". - Húsvét")
        else:
            nap = str(d + e - 9)
            print("Április " + nap + ". - Húsvét")

    else:
        print("Hibás évszámot adtál meg")
