import random
def paratlan_szam():
    szam = random.randint(40,150)
    while szam % 2 == 0:
       szam = random.randint(40,150)
    return szam

def lista():
    szamok = []
    for i in range(13):
        szamok.append(paratlan_szam())
    return szamok

def megszamlalas(szamok):
    db = 0
    for i in range(len(szamok)):
        if szamok[i] < 100:
            db += 1
    return db

def elvalasztas(szam):
    for i in range(len(szam)):
        if i == len(szam)-1:
            print(szam[i], end="")
        else: 
            print(szam[i], end="*")

def faljba_iras(szamok):
    with open ("ketjegyu.txt", "w", encoding="utf-8") as file:
        file.write(f"A kétjegyűek száma:{megszamlalas(szamok)}")
        file.close()
    

def teljes():
    szamok = lista()
    print(megszamlalas(szamok))
    elval = elvalasztas(szamok)
    print(elval)
    faljba_iras(szamok)