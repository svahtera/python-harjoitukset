import random

def d6():
    roll=random.randint(1,6)
    return roll

result=0

while result!=6:
    result=d6()
    print(result)