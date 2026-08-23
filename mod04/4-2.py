cabin=str.upper(input("Mikä on hyttiluokkasi (LUX, A, B, C)? "))
if cabin=="LUX":
    print("Hyttisi on parvekkeellinen yläkannella.")
elif cabin=="A":
    print("Hyttisi on ikkunallinen autokannen yläpuolella.")
elif cabin=="B":
    print("Hyttisi on ikkunaton autokannen yläpuolella.")
elif cabin=="C":
    print("Hyttisi on ikkunaton autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")