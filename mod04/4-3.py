#Sukupuoli
t=False
while t==False:
    gen=str.upper(input("Biologinen sukupuolesi (M tai N): "))
    if gen=="M" or gen=="N":
        t=True

#Hemoglobiiniarvo
t=False
while t==False:
    glob=input("Hemoglobiiniarvosi (g/l): ")
    glo=glob.replace(",", ".")
    try:
        float(glob)
    except:
        print("Luku ei kelpaa. Syötä vain numeroita.")
    else:
        glob=float(glob)
        t=True

#tulos
if (gen=="M" and glob < 134) or (gen=="N" and glob < 117):
    print("Hemoglobiiniarvosi on matala.")
elif (gen=="M" and glob > 195) or (gen=="N" and glob > 175):
    print("Hemoglobiiniarvosi on korkea.")
else:
    print("Hemoglobiiniarvosi on normaali.")