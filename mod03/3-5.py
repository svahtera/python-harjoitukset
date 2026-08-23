#Yksiköiden alustus kilogrammoiksi
import math

#Lukujen syöttö
numTest=bool(False)
while numTest==False:
    leiviska=input("Anna leiviskät: ")
    leiviska=leiviska.replace(",", ".")
    try:
        float(leiviska)
    except:
        print("Luku ei kelpaa. Syötä vain numeroita.")
    else:
        leiviska=float(leiviska)
        numTest=True

numTest=bool(False)
while numTest==False:
    naula=input("Anna naula: ")
    naula=naula.replace(",", ".")
    try:
        float(naula)
    except:
        print("Luku ei kelpaa. Syötä vain numeroita.")
    else:
        naula=float(naula)
        numTest=True
        
numTest=bool(False)
while numTest==False:
    luoti=input("Anna luodit: ")
    luoti=luoti.replace(",", ".")
    try:
        float(luoti)
    except:
        print("Luku ei kelpaa. Syötä vain numeroita.")
    else:
        luoti=float(luoti)
        numTest=True

#Yksikkömuunnos
total=math.fma(leiviska, 8.512, math.fma(naula, .4256, math.fma(luoti, .0133, 0.0)))
kilograms=int(total)
grams=round((total-kilograms)*1000)

#Tulostus
print(f"Massa nykymittojen mukaan:\n{kilograms} kilogrammaa ja {grams} grammaa.")