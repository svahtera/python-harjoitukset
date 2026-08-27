dictAirports={
}
sEntry=""
sExit="Kiitos käynnistä!"

def newAirport ():
    sNameIn=str.capitalize(input("Lentoaseman nimi: "))
    sCodeIn=str.upper(input("ICAO: "))
    dictAirports[sCodeIn]=sNameIn

while sEntry!="L" or sEntry!="U" or sEntry!="H":
    sEntry=str.upper(input("(U)usi, (H)aku vai (L)opeta? "))
    if sEntry=="L":
        break
    elif sEntry=="U":
        newAirport()
    elif sEntry=="H":
        if dictAirports=={}:
            break
        sQuery=str.upper(input("Hae lentokenttä: "))
        if sQuery in dictAirports:
            print(f"{sQuery}: {dictAirports[sQuery]}")
        else:
            print(f"Lentokenttää {sQuery} ei löytynyt.")
print(sExit)