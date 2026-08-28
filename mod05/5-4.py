import random

guess=0
score=int(random.randint(1,10))

while guess !=score:
    guess=int(input("Arvaa luku (1-10)"))
    if guess<score:
        print("Liian pieni arvaus")
    else:
        print("Liian suuri arvaus")

print("Oikein!")