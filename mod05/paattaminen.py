sCom=input("Anna komento: ")
while str.upper(sCom) != "LOPETA":
    if str.upper(sCom)=="MAYDAY":
        break
    print("Suoritan komennon " + sCom)
    sCom=input("Anna komento: ")
else:
    print("Näkemiin.")
print("Toiminnot lopetettu.")