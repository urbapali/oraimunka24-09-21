print("Szia")

evszam = int(input("Adj meg egy évszámot 1900-2099 között: \n"))

a = evszam % 19
b = evszam % 4
c = evszam % 7

m, n = 0, 0

if 1583 <= evszam <= 1699:
    m = 22
    n = 2
elif evszam <= 1799:
    m = 23
    n = 3
elif evszam <= 1899:
    m = 23
    n = 4
elif evszam <= 2099:
    m = 24
    n = 5
elif evszam <= 2199:
    m = 24
    n = 6
elif evszam <= 2299:
    m = 25
    n = 0

if 1900 <= evszam <= 2099:
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
