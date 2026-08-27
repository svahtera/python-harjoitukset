dictAirports={}
sExitMsg="Kiitos Käynnistä"
sEntry=""

def newAirport ():
    sNameIn=input("Lentoaseman nimi: ")
    sCodeIn=str.capitalize(input("ICAO: "))
    dictAirports[sNameIn]=sCodeIn
    
#while sEntry!="L" or sQuery!="U":
sEntry=str.capitalize(input("(U)usi vai (L)opeta? "))
while sEntry!="L" or sEntry!="U" or sEntry!="H":
    if sEntry=="L":
        exit(sExitMsg)
    elif sEntry=="U":
        newAirport()
    elif sEntry=="H":
        sQuery=input("Hae lentokenttä: ")
        if sQuery in dictAirports:
            print(f"{sQuery}: {dictAirports[sQuery]}")
    sEntry=str.capitalize(input("(U)usi, (H)aku vai (L)opeta? "))
