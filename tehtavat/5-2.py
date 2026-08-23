import math

len=0.0
while len>=0:
    t=False
    while t==False:
        len=input("Syötä pituus tuumina: ")
        try:
            float(len)
        except:
            print("Luku ei kelpaa. Syötä vain numeroita.")
        else:
            t=True
    len=math.fma(float(len), 2.54,0)
    print(f"{len}cm")
    
