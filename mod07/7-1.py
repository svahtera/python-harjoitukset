import random

def d6():
    roll=random.randint(1,6)
    return roll

t=False
while t==False:
    num=input("Kuinka montaa noppaa heitetään? ")
    try:
        int(num)
    except:
        print("Luku ei kelpaa. Syötä vain numeroita.")
    else:
        t=True
        num=int(num)

for i in range(num):
    print(d6())