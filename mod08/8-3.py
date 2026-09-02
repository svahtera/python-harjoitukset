dictAirports={
}
sEntry=""

def newAirport ():
    sNameIn=str.capitalize(input("Lentoaseman nimi: "))
    sCodeIn=str.upper(input("ICAO: "))
    dictAirports[sCodeIn]=sNameIn

#Pääsilmukka
sEntry==""
while sEntry!="L":
    sEntry=str.upper(input("(U)usi, (H)aku vai (L)opeta? "))
    if sEntry=="U":
        newAirport()
    if sEntry=="H":
        if dictAirports!={}:    #keskeytä haku jos lentokenttiä ei ole lisätty
            sQuery=str.upper(input("Hae lentokenttä: "))
            if sQuery in dictAirports:
                print(f"{sQuery}: {dictAirports[sQuery]}")
            else:
                print(f"Lentokenttää {sQuery} ei löytynyt.")
        else:
            print("Syötä ensin lentokenttä.")
print("Kiitos käynnistä")