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
    szoveg = ""
    for i in range(len(szam)):
        if i == len(szam)-1:
            szoveg += str(szam[i])
        else: 
            szoveg += str(szam[i]) + "*"
    return szoveg

def faljba_iras(szamok):
    with open ("ketjegyu.txt", "w", encoding="utf-8") as file:
        file.write(f"A kétjegyűek száma:{megszamlalas(szamok)}")
        file.close()
    

def teljes():
    szamok = lista()
    elval = elvalasztas(szamok)
    megszam = megszamlalas(szamok)
    print("II/a,c")
    print(f"\t{elval}")
    print("II/b")
    print(f"\t{megszam}")
    faljba_iras(szamok)