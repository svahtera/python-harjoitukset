import random

n=int(input("Kuinka monta noppaa haluat heittää? "))

i=0
total=0
for i in range(int(n)):
    total=total+random.randint(1,6)
print(total)