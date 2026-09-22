
numTest=bool(False)
length=int(input("Anna suorakulmion kanta: "))
height=int(input("Anna suorakulmion korkeus: "))
circumference=2*(length+height)
area=length*height

#Tulostus
print(f"{'Suorakulmion piiri on '}{circumference:.2f}\n{'Suorakulmion pinta-ala on '}{area:.2f}")