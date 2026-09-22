import math

gal=0
litre=0

#Muunnosfunktio
def conv(gal):
    litre=gal * 3.785
    return litre

while gal>=0:
    gal=float(input("Kuinka monta gallonaa? "))
    print(f"{conv(gal)} litraa")