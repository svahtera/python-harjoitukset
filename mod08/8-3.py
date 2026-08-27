dictAirports={}
sExitMsg="Kiitos Käynnistä"
sQuery=""

def newAirport ():
    sNameIn=input("Lentoaseman nimi: ")
    sCodeIn=str.capitalize(input("ICAO: "))
    dictAirports[sNameIn]=sCodeIn
    
while sQuery!="L" or sQuery!="U":
    sQuery=str.capitalize(input("(U)usi vai (L)opeta? "))
while sQuery!="L" or sQuery!="U" or sQuery!="H":
    if sQuery=="L":
        exit(sExitMsg)
    elif sQuery=="U":
        newAirport()
        print(dictAirports)
    elif sQuery=="H":
        pass
    sQuery=str.capitalize(input("(U)usi, (H)aku vai (L)opeta? "))
