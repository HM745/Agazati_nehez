def bekeres(i):
    szam = int(input(f"Adja meg a(z) {i+1} negatív egész számot: "))
    while szam > -1:
        szam = int(input(f"Adja meg a(z) {i+1} negatív egész számot: "))
    return szam

def lista():
    szamok = []
    for i in range(3):
        szamok.append(bekeres(i))
    return szamok

def megszamlalas(szam):
    min_index = 0
    for i in range(len(szam)):
        if szam[min_index]**2 < szam[i]:
            min_index = i
    return min_index

def teljes():
    szamok = lista()
    megszam = megszamlalas(szamok)
    print(szamok)
    print(f"A legkisebb négyzetű szám: {szamok[megszam]} megadási sorrendje:{megszam+1}")