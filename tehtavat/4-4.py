t=False
while t==False:
    year=input("Syötä vuosiluku: ")
    year=year.replace(",", ".")
    try:
        int(year)
    except:
        print("Luku ei kelpaa. Syötä vain numeroita.")
    else:
        year=int(year)
        t=True

if year/4==int(year/4) and (year/100==int(year/100) and year/400==int(year/400)):
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")