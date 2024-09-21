print("Szia")

szam = int(input("Adj meg egy számot 1-12 között: "))

honapok = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június', 'Július', 'Augusztus', 'Szeptember', 'Október', 'November', 'December']

if(szam >= 1 and szam <= 12):
    print("A hónap: " + honapok[szam-1])
else:
    print("Hibás számot adtál meg")


evszam = int(input("Adj meg egy évszámot: "))
a = evszam % 19
b = evszam % 4
c = evszam % 7

d = ((19 * a) + M) % 30
e = ((2*b) + (4*c) + (6*d) + N ) % 7
