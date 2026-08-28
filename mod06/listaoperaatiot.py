lNames=["Make", "Viljami", "Viljamin Veli"]

sCom=input("(L)istaa, (U)usi nimi, (P)oista tai lopeta (ENTER): ")

def printList():
    n=0
    i=0
    for n in lNames:
        i=i+1
        print(f"{i:4}: {n}")


while sCom!="":
    if str.upper(sCom)=="L":
        printList()
    if str.upper(sCom)=="U":
        sName=input("Anna lisättävä nimi: ")
        lNames.append(sName)
    if str.upper(sCom)=="P":
        sName=input("Anna poistettava nimi tai järjestysnumero: ")
        if sName in lNames:
            lNames.remove(sName)
        try:
            int(sName)
        except:
            pass
        else:
            sName=int(sName)
            if sName<=len(lNames):
                print(f"{lNames[int(sName)-1]} poistettu.")
                lNames.pop(int(sName)-1)
            else:
                print("Lista ei ole niin pitkä.")
    sCom=input("(L)istaa, (U)usi nimi, (P)oista tai lopeta (ENTER): ")

printList()