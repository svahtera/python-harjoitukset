import roomdat

import json
import os

#Muuttujien alustus
playerInput=""
bRunning=True

##Asetukset ja pelaaja
class Player:
    def __init__(self, sName, iAge, bBones, location, inventory=[]):
        self.sName=sName
        self.iAge=iAge
        self.bBones=bBones
        self.inventory=inventory
        self.location=location

##Esineet
class Item():
    def __init__(self, sName, fWeight):
        self.sName=sName
        self.fWeight=fWeight

    #Listaus
    def show():
        print("\nKannat:")
        if pelaaja.inventory!=[]:
            num=0
            for i in pelaaja.inventory:
                num=num+1
                print(f"{num}. {i}")
            itemUsed=input(f"Käytä esinettä? (1-{num})\n")
            
            try:
                itemUsed=int(itemUsed)-1
            except:
                #Ohita jos syöte ei ole numero
                pass
            else:
                if 0<itemUsed<=len(pelaaja.inventory):
                    print(f"Käytät {pelaaja.inventory[itemUsed]}.")

        else:
            print("Ei mitään")

    #Keräys
    def take():
        sItemTaken=str.capitalize(input("Kerää esine: "))

        #Jos esine on olemassa, se lisätään pelaajalle
        #Jos ei, kerrotaan ettei sitä ole

        if sItemTaken in pelaaja.location["Items"]:
            pelaaja.inventory.append(sItemTaken)
            pelaaja.location["Items"].remove(sItemTaken)
            print(f"Keräät esineen {sItemTaken}.")
        else:
            print(f"Et löydä esinettä {sItemTaken}.")
    

#Huoneet
#Odottaa poistoa
class Room():
    def __init__(self, sName, sDesc, items, lDest):
        self.sName=sName    #Huoneen nimi
        self.sDesc=sDesc    #Huoneen teksti
        self.items=items    #Esineet jotka pelaaja voi kerätä
        self.lDest=lDest    #Huoneen naapurit

    def menu():
        pass
        #Tähän komentojen jne tulostus.

#Pelaajan alustus

intTest=False
bBones=False
bContinue=False

sName=input("Nimesi: ")
sSavePath=(f"./peliprojekti/save/{sName}.json")

#Kysy tallennuksen jatkamista
if os.path.exists(sSavePath):
    playerInput=input("Jatka tallennuksesta? Y, tai mitä tahansa muuta aloittaaksesi uusi.\n")
    if str.upper(playerInput)=="Y":
        bContinue=True
        with open(sSavePath, "r") as saveFile:
            saveData=json.load(saveFile)
        sName=saveData["sName"]
        iAge=saveData["iAge"]
        bBones=saveData["bBones"]
        location=saveData["location"]
        inventory=saveData["inventory"]
        for i in roomdat.dictRooms:
            if i["Name"]==location:
                location=i
        pelaaja=Player(sName, iAge, bBones, location, inventory)


#Uusi pelaaja
if bContinue==False:
    #Kysy ikää kunnes pelaaja syöttää luvun 
    while intTest==False:
        iAge=input("Ikäsi: ")
        try:
            iAge=int(iAge)
        except:
            print("Syötä oikea luku")
        else:
            intTest=True
    playerInput=input("Luut? Y, tai mikä tahansa muu jatkaaksesi ilman.")
    if str.upper(playerInput)=="Y":
        bBones=True
    location=roomdat.dictRooms[0]
    pelaaja=Player(sName, iAge, bBones)

    #Ikäportti
    if pelaaja.iAge < 12:
        exit(f"Kiitos mielenkiinnostasi {pelaaja.sName}, mutta tämän ohjelman ikäraja on 12.")
    else:
        print(f"\nTerve {pelaaja.sName}! Ikäsi on {pelaaja.iAge}.\n")

#pelaaja.location=roomdat.dictRooms[0]

##Pääsilumukka

while bRunning == True:
    print(f"\n{pelaaja.location["Name"]}\n{pelaaja.location["Desc"]}")
    print(f"\n1. Liiku\n2. Kerää\n3. Esineet\n\ntai LOPETA")

    playerInput=input()

    #Liike

    if playerInput=="1":

        #Jos pelaajalla on luut, kysytään mihin mennään. Jos ei ole, pelaaja ei voi liikkua

        #Jos on, tarkastetaan pääseekö nykysijainnista kohteeseen, ja annetaan pelaajalle uusi sijainti

        if pelaaja.bBones==True:
            sTarget=str.capitalize(input("\nMihin haluat liikkua? "))
            if sTarget in pelaaja.location["Dest"]:
                    for i in roomdat.dictRooms:
                        if i["Name"]==sTarget:
                            pelaaja.location=i
            else:
                print(f"Et löydä paikkaa {sTarget}.")
        else:
            print("\nSinulla ei ole luita. Olet kykenemätön liikkumana omin voimin.")

    #Inventaario-operaatiot
    if playerInput=="2":
        Item.take()
    if playerInput=="3":
        Item.show()

    #Lopetus
    if str.upper(playerInput)=="LOPETA":
        bRunning=False

#Lopetus
playerInput=input("Haluatko tallentaa?  Syötä Y, tai mitä tahansa muuta lopettaaksesi tallentamatta.\n")
if str.upper(playerInput)=="Y":
    saveData={
        "sName":pelaaja.sName,
        "iAge":pelaaja.iAge,
        "bBones":pelaaja.bBones,
        "inventory":pelaaja.inventory,
        "location":pelaaja.location["Name"]
    }
    print("\n Tallennettu!")
    with open(sSavePath, "w") as saveFile:
        json.dump(saveData, saveFile)
print("Kiitos käynnistä!")