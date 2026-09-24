##Asetukset ja pelaaja
class Player:
    def __init__(self, sName, iAge):
        self.inventory=[]
        self.sName=sName
        self.iAge=iAge
        self.sLocation=""

    #Alustus
    sHyperMenuState="suljettu"
    bHyperMenuOpen=False
    sAwesomenessDetectionState="epäaktiivinen"
    bAwesomenessDetection=False

    bBones=False
    sBonesState="pois"

    #Pelin tilaan liittyviä muuttujia
    
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

#Pelaaja

##Esineet
class Item():
    items=[]
    def __init__(self, sName, fWeight):
        self.sName=sName
        self.fWeight=fWeight
        

    #Listaus
    def show():
        print("\nKannat:")
        for i in pelaaja.inventory:
            print("> "+ i)
        print()

#Huoneet
class Room():

    def __init__(self, items, lDest=[], sName="PENKINLÄMMITTÄJÄ", sDesc="Olet muodottomassa testitilassa."):
        self.sName=sName    #Huoneen nimi
        self.sDesc=sDesc    #Huoneen teksti
        self.items=items    #Esineet jotka pelaaja voi kerätä
        self.lDest=lDest    #Huoneen naapurit

    def menu(self):

        #Tähän komentojen jne tulostus.
        print(f"{self.sName}\n{self.sDesc}")
        print(f"\n1. Liiku\n2. Kerää\n3. Listaa esineet\n\ntai LOPETA")
        playerInput=input()

        if playerInput=="1":                        #Pelaaja valutsee liikkua
            if Player.bBones==True:                 
                print("\nLiikut testitilassa.") 
                sTarget=input("\nMihin haluat liikkua? ")
                if sTarget in self.lDest:
                    pelaaja.sLocation=sTarget
                else:
                    print(f"Et pääse tilaan {sTarget}.")
            else:
                print("\nSinulla ei ole luita. Olet kykenemätön liikkumana omin voimin.")
        if playerInput=="2":                        #Pelaaja kerää esineen...
            sItemTaken=input("Kerää esine: ")
            if sItemTaken in self.items:                #joka on olemassa
                pelaaja.inventory.append(sItemTaken)
                self.items.remove(sItemTaken)
        else:                                       #Joka ei ole olemassa
            print(f"Et löydä esinettä {sItemTaken}.")
        if playerInput=="3":                        #Esineiden listaus
            Item.show()
        if str.upper(playerInput)=="LOPETA":        #Lopetus
            exit("Kiitos känyynistä")

testspace=Room(["Urheilu Almanakka 1985", "TT-33"])

#Muuttujien alustus
playerInput=""

#Tehtävä 1
#Nimen ja iän tallennus
sName=input("Nimesi: ")
iAge=int(input("Ikäsi: "))

pelaaja=Player(sName, iAge)

#Tehtävä 2
#Iän tarkastus
if pelaaja.iAge < 12:
    exit(f"Kiitos mielenkiinnostasi {pelaaja.sName}, mutta tämän ohjelman ikäraja on 12.")
else:
    print(f"Terve {pelaaja.sName}! Ikäsi on {pelaaja.iAge}.\n")

##Main Menu
while playerInput!="1":
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