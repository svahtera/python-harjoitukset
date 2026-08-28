import random
import math

N=int(input("Kuinka monta pistettä haluat arpoa? "))    

n=0
for i in range(N+1):
    xPos=random.triangular(-1, 1)
    yPos=random.triangular(-1, 1)
    if xPos**2+yPos**2<1:
        n=int(n+1)
aprox=4*n/N
print(f'{"Piin likiarvo on"} {aprox}')