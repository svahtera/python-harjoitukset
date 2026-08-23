import random
import math

A=1

t=False
while t==False:
    N=input("Kuinka monta pistettä haluat arpoa? ")
    try:
        int(N)
    except:
        print("Luku ei kelpaa. Syötä vain numeroita.")
    else:
        t=True
        N=int(N)

#i=0
n=0
for i in range(N+1):
    xPos=random.triangular(-1, 1)
    yPos=random.triangular(-1, 1)
    if xPos**2+yPos**2<1:
        n=int(n+1)
aprox=4*n/N
print(f'{"Piin likiarvo on"} {aprox}')