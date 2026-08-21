lengthStr=input("Anna suorakulmion kanta: ")
heightStr=input("Anna suorakulmion korkeus: ")

length=float(lengthStr)
height=float(heightStr)
circumference=2*(length+height)
area=length*height

print(f"{'Suorakulmion piiri on '}{circumference:.2f}")
print(f"{'Suorakulmion pinta-ala on '}{area:.2f}")