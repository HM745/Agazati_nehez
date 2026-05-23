import osztaly

def beolvasas():
    with open ("stadionok.txt", "r", encoding="utf-8") as file:
        sorok = file.readlines()
    return sorok

def obj_lista(lista:list) -> list[osztaly.Stadionok]:
    adatok = []
    for i in range(1, len(lista)):
        sor = lista[i].strip().split(";")
        stadionok = osztaly.Stadionok(
            sor[0],
            sor[1],
            sor[2],
            sor[3],
            sor[4]
        )
        adatok.append(stadionok)
    return adatok

def csapatok(csapat:list[osztaly.Stadionok]):
    db = 0
    for i in range(len(csapat)):
        db += 1
    return db

def kivaLasztas(new_york_cspat:list[osztaly.Stadionok]):
    new_york = []
    for i in range(len(new_york_cspat)):
        if new_york_cspat[i].varos == "New York":
            new_york.append(new_york_cspat[i])
    return new_york

def september(sep:list[osztaly.Stadionok], honap: str):
    db = 0
    for i in range(len(sep)):
        datum = sep[i].elso_merkozes.split("-")
        if datum[1] == honap:
            db += 1 
    return db

def teljes():
    sor = beolvasas()
    obj = obj_lista(sor)
    csapatok_szama = csapatok(obj)
    csapatok1 = kivaLasztas(obj)
    honap = september(obj, "09")
    print("III/b")
    print(f"\tA csapatok: darabszáma: {csapatok_szama}")
    print("III/c")
    for i in csapatok1:
        print(f"\t{i.nev} - {i.csapat_szam}")
    print("III/d")
    print(f"\tA szeptemberi kezdő mérkőzések száma: {honap}")