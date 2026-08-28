import random

i=0
rollsTotal=0

while i<100000:
    die1=die2=rolls=0
    while die1!=6 or die2!=6:
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        rolls=rolls+1
    #print(f"Tarvittiin {rolls} heittoa")
    i=i+1
    rollsTotal=rollsTotal+rolls

rollsAvg=(rollsTotal/i)
print(f"Heitot keskimäärin: {rollsAvg:6.4f}")