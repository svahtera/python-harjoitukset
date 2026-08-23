import math

numTest=bool(False)
while numTest==False:
    radius=input("Anna ympyrän säde: ")
    radius=radius.replace(",", ".")
    try:
        float(radius)
    except:
        print("Luku ei kelpaa. Syötä vain numeroita.")
    else:
        numTest=True
        radius=float(radius)
pi=math.pi
area=2*pi*radius
print(f"{'Ympyrän pinta-ala on '}{area:.2f}.")