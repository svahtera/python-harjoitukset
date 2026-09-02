import math
pi=math.pi

#Arvon lasku
def pricePerArea (diameter, price):
    radius=diameter/100/2   #Halkaisija neliömetreinä
    area=pi*radius**2
    value=price/area
    return value

#Lukujen syöttö
diameter1=float(input("Ensimmäisen pizzan halkaisija (cm) "))
price1=float(input("Ensimmäisen pizzan hinta (euroa) "))
diameter2=float(input("Toisen pizzan halkaisija (cm) "))
price2=float(input("Toisen pizzan hinta (euroa) "))

#Vertailu ja tulostus
value1=pricePerArea(diameter1, price1)
value2=pricePerArea(diameter2, price2)

if value1 < value2:
    print(f'Ensimmäinen pizza on edullisempi hintaan {value1:.2f}€/m²')
else:
    print(f'Toinen pizza on edullisempi hintaan {value2:.2f}€/m²')
