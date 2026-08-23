#Lue luvut
numTest=bool(False)
while numTest==False:
    length=input("Anna suorakulmion kanta: ")
    length=length.replace(",", ".")
    try:
        float(length)
    except:
        print("Luku ei kelpaa. Syötä vain numeroita.")
    else:
        length=float(length)
        numTest=True
numTest=bool(False)
while numTest==False:
    height=input("Anna suorakulmion korkeus: ")
    height=height.replace(",", ".")
    try:
        float(height)
    except:
        print("Luku ei kelpaa. Syötä vain numeroita.")
    else:
        height=float(height)
        numTest=True

#Laskut
circumference=2*(length+height)
area=length*height

#Tulostus
print(f"{'Suorakulmion piiri on '}{circumference:.2f}\n{'Suorakulmion pinta-ala on '}{area:.2f}")