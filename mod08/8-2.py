sName=input("Anna nimi ")
lName=set()
while sName != "":
    if sName in lName:
        print("Aiemmin syötetty nimi.")
    else:
        lName.append(sName)
        print("Uusi nimi.")
    sName=input("Anna nimi ")
for i in lName:
    print(i)