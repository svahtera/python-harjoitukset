import math

#Luvunsyöttöfunktio
def numIn(query):
    t=False
    while t==False:
        num=input(query)
        num=num.replace(",", ".")
        try:
            float(num)
        except:
            print("Luku ei kelpaa. syötä vain numeroita.")
        else:
            num=float(num)
            t=True
    return num

#Lukujen syöttö
leiviska=numIn("Anna leiviskät: ")
naula=numIn("Anna naulat: ")
luoti=numIn("Anna luodit: ")

#Yksikkömuunnos
total=math.fma(leiviska, 8.512, math.fma(naula, .4256, math.fma(luoti, .0133, 0.0)))
kilograms=int(total)
grams=round((total-kilograms)*1000)

#Tulostus
print(f"Massa nykymittojen mukaan:\n{kilograms} kilogrammaa ja {grams} grammaa.")