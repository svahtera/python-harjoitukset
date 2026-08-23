import random

t=False
while t==False:
    n=input("Kuinka monta noppaa haluat heittää? ")
    try:
        int(n)
    except:
        print("Luku ei kelpaa. Syötä vain numeroita.")
    else:
        t=True

i=0
total=0
for i in range(int(n)):
    total=total+random.randint(1,6)
    print(total)