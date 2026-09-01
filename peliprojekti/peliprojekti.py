#Muuttujien alustus
lInventory=[]
playerInput=""

sHyperMenuState="suljettu"
bHyperMenuOpen=False

sAwesomenessDetectionState="epäaktiivinen"
bAwesomenessDetection=False

sBonesState="pois"
bBones=False

##Asetukset
#Hypervalikon status
def hypermenu(bHyperMenuOpen):
    if bHyperMenuOpen==False:
        bHyperMenuOpen=True
        sHyperMenuState="epäsuljettu"
        print(f"\nHypervalikko epäsuljettu")
    else:
        bHyperMenuOpen=False
        sHyperMenuState="suljettu"
        print(f"\nHypervalikko suljettu")
    return bHyperMenuOpen, sHyperMenuState

#Siisteydentunnistuksen status
def awesomenessDetection(bAwesomenessDetection):
    if bAwesomenessDetection==False:
        bAwesomenessDetection=True
        sAwesomenessDetectionState="aktiivinen"
        print(f"\nSiisteydentunnistus aktivoitu")
    else:
        bAwesomenessDetection=False
        sAwesomenessDetectionState="epäaktiivinen"
        print(f"\nSiisteydentunnistus epäaktivoitu")
    return bAwesomenessDetection, sAwesomenessDetectionState

#luiden status
def bones(bBones):
    if bBones==False:
        bBones=True
        sBonesState="päällä"
        print(f"Luut kytketty")
    else:
        bBones=False
        sBonesState="pois"
        print(f"Luut poistettu")
    return bBones, sBonesState

##inventory
#Keräys
def inventoryTake():
    #Kun huoneet on implementoitu, tässä on paikka tarkastaa löytyykö esineitä
    lInventory.append(input("\nKerää esine: "))

#Listaus
def inventoryPrint():
    print("\nKannat:")
    for i in lInventory:
        print("> "+ i)

#Tehtävä 1
#Nimen ja iän tallennus
sPlayerName=input("Nimesi: ")
iPlayerAge=int(input("Ikäsi: "))

#Tehtävä 2
#Iän tarkastus
if iPlayerAge < 12:
    exit(f"Kiitos mielenkiinnostasi {sPlayerName}, mutta tämän ohjelman ikäraja on 12.")
else:
    print(f"Terve {sPlayerName}! Ikäsi on {iPlayerAge}.\n")

##Main Menu
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
        if bBones==True:
            print("\nLiikut testitilassa.")
            #Liike tähän myöhemmin
        else:
            print("\nSinulla ei ole luita. Olet kykenemätön liikkumana omin voimin.")
    if playerInput=="2":
        inventoryTake()
    if playerInput=="3":
        inventoryPrint()
        
print("Ohjelman loppu")