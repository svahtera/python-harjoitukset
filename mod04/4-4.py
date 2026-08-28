year=int(input("Syötä vuosiluku: "))

if year/4==int(year/4) and (year/100==int(year/100) and year/400==int(year/400)):
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")