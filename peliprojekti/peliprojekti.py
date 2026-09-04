##Asetukset
class Option:
    #Alustus
    sHyperMenuState="suljettu"
    bHyperMenuOpen=False

    sAwesomenessDetectionState="epäaktiivinen"
    bAwesomenessDetection=False
    
    #Hypervalikon status
    def hypermenu():
        if Option.bHyperMenuOpen==False:
            Option.bHyperMenuOpen=True
            Option.sHyperMenuState="epäsuljettu"
            print(f"\nHypervalikko epäsuljettu")
        else:
            Option.bHyperMenuOpen=False
            Option.sHyperMenuState="suljettu"
            print(f"\nHypervalikko suljettu")
        return

    #Siisteydentunnistuksen status
    def awesomenessDetection():
        if Option.bAwesomenessDetection==False:
            Option.bAwesomenessDetection=True
            Option.sAwesomenessDetectionState="aktiivinen"
            print(f"\nSiisteydentunnistus aktivoitu")
        else:
            Option.bAwesomenessDetection=False
            Option.sAwesomenessDetectionState="epäaktiivinen"
            print(f"\nSiisteydentunnistus epäaktivoitu")
        return

    #luiden status
    #Lähettää luiden tilan pelaajaluokkaan
    def bones():
        if Player.bBones==False:
            Player.bBones=True
            Player.sBonesState="päällä"
            print(f"Luut kytketty")
        else:
            Player.bBones=False
            Player.sBonesState="pois"
            print(f"Luut poistettu")
        return

#Pelaaja
class Player:
    #Alustus

    sName=""
    iAge=0

    bBones=False
    sBonesState="pois"

    sLocation=""

    def __init__():
        pass

##Esineet
class Item():
    inventory=set()   #Pelaajan esineet

    def __init__(self, sName):
        self.sName=sName

    #Keräys
    def take():
        #Kun huoneet on implementoitu, tässä on paikka tarkastaa löytyykö esineitä
        Item.inventory.add(input("\nKerää esine: "))

    #Listaus
    def show():
        print("\nKannat:")
        for i in Item.inventory:
            print("> "+ i)

#Huoneet
class Room():
    def __init__(self, sName="PENKINLÄMMITTÄJÄ", items=set(), obj=set, coms=set()):
        self.sName=sName
        self.items=items    #Esineet jotka pelaaja voi kerätä
        self.lObj=obj       #Kohteet joilla on interaktiot
        self.coms=coms      #Komennot


#Muuttujien alustus
playerInput=""

#Tehtävä 1
#Nimen ja iän tallennus
Player.sName=input("Nimesi: ")
Player.iAge=int(input("Ikäsi: "))

#Tehtävä 2
#Iän tarkastus
if Player.iAge < 12:
    exit(f"Kiitos mielenkiinnostasi {Player.sName}, mutta tämän ohjelman ikäraja on 12.")
else:
    print(f"Terve {Player.sName}! Ikäsi on {Player.iAge}.\n")

##Main Menu
while str.upper(playerInput)!="1":
    #teksti
    print("\nHIENO OTSIKKO\n")
    print(f"1. Aloita\n2. Hypervalikko {Option.sHyperMenuState}\n3. Siisteydentunnistus {Option.sAwesomenessDetectionState}\n4. Luut {Player.sBonesState}\n\ntai LOPETA")

    #valinnat
    playerInput=input()
    if playerInput=="2":
        Option.hypermenu()
    if playerInput=="3":
        Option.awesomenessDetection()
    if playerInput=="4":
        Option.bones()
    if str.upper(playerInput)=="LOPETA":
        exit("Kiitos käynnistä")

#Main Loop
while str.upper(playerInput)!="LOPETA":
    print(f"\n1. Liiku\n2. Kerää\n3. Listaa esineet\n\ntai LOPETA")

    #valinnat
    playerInput=input()
    if playerInput=="1":
        if Player.bBones==True:
            print("\nLiikut testitilassa.")
            #Liike tähän myöhemmin
        else:
            print("\nSinulla ei ole luita. Olet kykenemätön liikkumana omin voimin.")
    if playerInput=="2":
        Item.take()
    if playerInput=="3":
        Item.show()
        
print("Ohjelman loppu")