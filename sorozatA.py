def paratlan_szam():
    szam = int(input("Adj meg egy pártlan számot:"))
    while szam % 2 == 0:
        szam = int(input("Adj meg újra egy páratlan számot:"))
    return szam

