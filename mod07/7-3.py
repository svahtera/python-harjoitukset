import math

gal=0
litre=0

#Muunnosfunktio
def conv(gal):
    litre=math.fma(gal, 4.785, 0)
    return litre

while gal>=0:
    gal=float(input("Kuinka monta gallonaa? "))
    print(conv(gal))