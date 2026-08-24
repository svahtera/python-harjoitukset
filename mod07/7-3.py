import math

gal=0
litre=0

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

#Muunnosfunktio
def conv(gal):
    litre=math.fma(gal, 4.785, 0)
    return litre

while gal>=0:
    gal=float(input("Kuinka monta gallonaa? "))
    print(conv(gal))