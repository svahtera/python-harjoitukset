import random

guess=0
score=int(random.randint(1,10))

while guess !=score:
    guess=input("Arvaa luku (1-10)")
    t=False
    while t==False:
        try:
            int(guess)
        except:
            print("Luku ei kelpaa. Syötä vain numeroita.")
        else:
            t=True
            guess=int(guess)
    if guess<score:
        print("Liian pieni arvaus")
    else:
        print("Liian suuri arvaus")

print("Oikein!")