tSeason=("Talvi", "Kevät", "Kesä", "Syksy")

bT=False
while bT==False:
    iMonth=input("Anna kuukauden järjestysnumero (1-12): ")
    try:
        int(iMonth)
    except:
        print("Luku ei kelpaa. Syötä vain numeroita.")
    else:
        iMonth=int(iMonth)
        if iMonth >=1 and iMonth <= 12:
            bT=True

#Tähän vuodenajan määrittely
if iMonth == 12 or iMonth <= 2:
    print("Vuodenaika on talvi")
elif iMonth <= 5:
    print("Vuodenaika on kevät")
elif iMonth <= 8:
    print("Vuodenaika on kesä")
else:
    print("Vuodenaika on syksy.")