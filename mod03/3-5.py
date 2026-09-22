leiviska=float(input("Anna leiviskät: "))
naula=float(input("Anna naulat: "))
luoti=float(input("Anna luodit: "))

#Yksikkömuunnos
total=float(leiviska * 8.512 + naula * .4256 + luoti * .0133)
kilograms=int(total)
grams=round((total-kilograms)*1000)

#Tulostus
print(f"Massa nykymittojen mukaan:\n{kilograms} kilogrammaa ja {grams} grammaa.")