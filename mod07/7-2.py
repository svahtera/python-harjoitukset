import random

#noppa
def die():
    roll=random.randint(1,d)
    return roll

roll=0

t=False
while t==False:
    d=input("Kuinka mini tahkoista noppaa heitetään?")
    try:
        int(d)
    except:
        print("Luku ei kelpaa. Syötä vain numeroita.")
    else:
        t=True
        d=int(d)

roll=0
while roll != d:
    roll=die()
    print(roll)