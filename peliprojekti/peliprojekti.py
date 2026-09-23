##Asetukset
class Player:
    #Alustus
    sHyperMenuState="suljettu"
    bHyperMenuOpen=False
    sAwesomenessDetectionState="epäaktiivinen"
    bAwesomenessDetection=False

    sName=""
    iAge=0

    bBones=False
    sBonesState="pois"

    #Pelin tilaan liittyviä muuttujia
    sLocation=""    #Pelaajan sijainti
    inventory=[]   #Pelaajan esineet
    
    #Hypervalikon status
    def hypermenu():
        if Player.bHyperMenuOpen==False:
            Player.bHyperMenuOpen=True
            Player.sHyperMenuState="epäsuljettu"
            print(f"\nHypervalikko epäsuljettu")
        else:
            Player.bHyperMenuOpen=False
            Player.sHyperMenuState="suljettu"
            print(f"\nHypervalikko suljettu")
        return

    #Siisteydentunnistuksen status
    def awesomenessDetection():
        if Player.bAwesomenessDetection==False:
            Player.bAwesomenessDetection=True
            Player.sAwesomenessDetectionState="aktiivinen"
            print(f"\nSiisteydentunnistus aktivoitu")
        else:
            Player.bAwesomenessDetection=False
            Player.sAwesomenessDetectionState="epäaktiivinen"
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

##Esineet
class Item():
    def __init__(self, sName, fWeight):
        self.sName=sName
        self.fWeight=fWeight
        

    #Listaus
    def show():
        print("\nKannat:")
        for i in Player.inventory:
            print("> "+ i)

#Huoneet
class Room():
    def __init__(self, items, sName="PENKINLÄMMITTÄJÄ", sDesc="Olet muodottomassa testitilassa."):
        self.sName=sName
        self.sDesc=sDesc
        self.items=items    #Esineet jotka pelaaja voi kerätä

    def menu(self):
        playerInput=""

        #Tähän komentojen jne tulostus.
        while str.upper(playerInput)!="LOPETA":
            print(f"{self.sName}\n{self.sDesc}")
            print(f"\n1. Liiku\n2. Kerää\n3. Listaa esineet\n\ntai LOPETA")
            playerInput=input()

            if playerInput=="1":
                if Player.bBones==True:
                    print("\nLiikut testitilassa.")
                    #Liike tähän myöhemmin
                else:
                    print("\nSinulla ei ole luita. Olet kykenemätön liikkumana omin voimin.")
            if playerInput=="2":
                sItemTaken=input("Kerää esine: ")
                if sItemTaken in self.items:
                    Player.inventory.append(sItemTaken)
                    self.items.remove(sItemTaken)
                else:
                    print(f"Et löydä esinettä {sItemTaken}.")
            if playerInput=="3":
                Item.show()
        if str.upper(playerInput)=="LOPETA":
            exit("Kiitos känyynistä")

testspace=Room(["Urheilu Almanakka 1985", "TT-33"])

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
    print(f"1. Aloita\n2. Hypervalikko {Player.sHyperMenuState}\n3. Siisteydentunnistus {Player.sAwesomenessDetectionState}\n4. Luut {Player.sBonesState}\n\ntai LOPETA")

    #valinnat
    playerInput=input()
    if playerInput=="2":
        Player.hypermenu()
    if playerInput=="3":
        Player.awesomenessDetection()
    if playerInput=="4":
        Player.bones()
    if str.upper(playerInput)=="LOPETA":
        exit("Kiitos käynnistä")

testspace.menu()
#Main Loop