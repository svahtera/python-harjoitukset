#Sukupuoli
t=False
gen=str.upper(input("Biologinen sukupuolesi (M tai N): "))

#Hemoglobiiniarvo
t=False
glob=int(input("Hemoglobiiniarvosi (g/l): "))

#tulos
if (gen=="M" and glob < 134) or (gen=="N" and glob < 117):
    print("Hemoglobiiniarvosi on matala.")
elif (gen=="M" and glob > 195) or (gen=="N" and glob > 175):
    print("Hemoglobiiniarvosi on korkea.")
elif gen=="M" or gen=="N":
    print("Hemoglobiiniarvosi on normaali.")
else:
    print("Tarkasta antamasi tiedot")