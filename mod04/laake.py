fWeight=0

iAge=int(input("Mikä on ikäsi? "))
if 15<=iAge<18:
    fWeight=float(input("Mikä on painosi? "))
if (iAge>=15 and fWeight>=55) or iAge>=18:
    print("Lääkkeen käyttö on sallittua.")
else:
    print("Lääkettä ei saa käyttää.")