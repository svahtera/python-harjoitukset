##Asetukset
#Hypervalikon status
sHyperMenuState="suljettu"
bHyperMenuOpen=False
def hypermenu(bHyperMenuOpen):
    if bHyperMenuOpen==False:
        bHyperMenuOpen=True
        sHyperMenuState="epäsuljettu"
    else:
        bHyperMenuOpen=False
        sHyperMenuState="suljettu"
    return bHyperMenuOpen, sHyperMenuState

#Siisteydentunnistuksen status
sAwesomenessDetectionState="epäaktiivinen"
bAwesomenessDetection=False
def awesomenessDetection(bAwesomenessDetection):
    if bAwesomenessDetection==False:
        bAwesomenessDetection=True
        sAwesomenessDetectionState="aktiivinen"
    else:
        bAwesomenessDetection=False
        sAwesomenessDetectionState="epäaktiivinen"
    return bAwesomenessDetection, sAwesomenessDetectionState

#luiden status
sBonesState="pois"
bBones=False
def bones(bBones):
    if bBones==False:
        bBones=True
        sBonesState="päällä"
    else:
        bBones=False
        sBonesState="pois"
    return bBones, sBonesState

##inventory
#Keräys
lInventory=[]
def inventoryTake():
    lInventory.append((input("\nKerää esine: ")))

#Listaus
def inventoryPrint():
    print("\nKannat:")
    for i in lInventory:
        print("> "+ i)


playerInput=""

playerName=input("Nimesi: ")
playerAge=int(input("Ikäsi: "))

if playerAge < 12:
    exit(f"Kiitos mielenkiinnostasi {playerName}, mutta tämän ohjelman ikäraja on 12.")
else:
    print(f"Terve {playerName}! Ikäsi on {playerAge}.\n")

#mainMenu
while str.upper(playerInput)!="1":
    #teksti
    print("\nHIENO OTSIKKO\n")
    print(f"1. Aloita\n2. Hypervalikko {sHyperMenuState}\n3. Siisteydentunnistus {sAwesomenessDetectionState}\n4. Luut {sBonesState}\n\ntai LOPETA")

    #valinnat
    playerInput=input()
    if playerInput=="2":
        bHyperMenuOpen, sHyperMenuState=hypermenu(bHyperMenuOpen)
    if playerInput=="3":
        bAwesomenessDetection, sAwesomenessDetectionState=awesomenessDetection(bAwesomenessDetection)
    if playerInput=="4":
        bBones, sBonesState=bones(bBones)
    if str.upper(playerInput)=="LOPETA":
        exit("Kiitos käynnistä")

#Main Loop
while str.upper(playerInput)!="LOPETA":
    print(f"\n1. Liiku\n2. Kerää\n3. Listaa esineet\n\ntai LOPETA")

    #valinnat
    playerInput=input()
    if playerInput=="1":
        print("\nLiikut testitilassa.")
    if playerInput=="2":
        inventoryTake()
    if playerInput=="3":
        inventoryPrint()
        
print("Ohjelman loppu")