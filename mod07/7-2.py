import random

#noppa
def die():
    roll=random.randint(1,d)
    return roll

roll=0
d=int(input("Kuinka moni tahkoista noppaa heitetään? <"))

roll=0
while roll != d:
    roll=die()
    print(roll)