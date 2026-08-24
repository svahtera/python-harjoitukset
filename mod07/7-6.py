import math
pi=math.pi

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

#Arvon lasku
def pricePerArea (diameter, price):
    value=diameter/2*pi**2/price
    return value

#Lukujen syöttö
diameter1=numIn("Ensimmäisen pizzan halkaisija (cm) ")
price1=numIn("Ensimmäisen pizzan hinta (euroa) ")
diameter2=numIn("Ensimmäisen pizzan halkaisija (cm) ")
price2=numIn("Ensimmäisen pizzan hinta (euroa) ")

#Vertailu ja tulostus
value1=pricePerArea(diameter1, price1)
value2=pricePerArea(diameter2, price2)

if value1 < value2:
    print(f'Ensimmäinen pizza on edullisempi hintaan {value1:.2f}/cm²')
else:
    print(f'Toinen pizza on edullisempi hintaan {value2:.2f}/cm²')
