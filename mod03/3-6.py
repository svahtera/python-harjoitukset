import random

i=0
code1=str()
while i < 3:
    code1=code1+str(random.randint(0, 9))
    i=i+1

i=0
code2=str()
while i < 4:
    code2=code2+str(random.randint(1, 6))
    i=i+1

print(f"Koodisi ovat:\n{code1}\n{code2}")