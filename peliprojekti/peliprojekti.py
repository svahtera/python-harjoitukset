import roomdat

import json
import os

#Muuttujien alustus
playerInput=""
bRunning=True
bWin=False

##Asetukset ja pelaaja
class Player:
    def __init__(self, sName, iAge, bBones, location, inventory=[], usedItems=[]):
        self.sName=sName
        self.iAge=iAge
        self.bBones=bBones
        self.location=location
        self.inventory=inventory
        self.usedItems=usedItems

    def move():
        #Jos pelaajalla on luut, kysytään mihin mennään. Jos ei ole, pelaaja ei voi liikkua

        #Jos on, tarkastetaan pääseekö nykysijainnista kohteeseen, ja annetaan pelaajalle uusi sijainti

        if pelaaja.bBones==True:

            #Minne mennään?
            sTarget=str.capitalize(input("\nMihin haluat liikkua? "))
            if sTarget in pelaaja.location["Dest"]:
                    for i in roomdat.dictRooms:
                        if i["Name"]==sTarget:

                            #Ei avainta, suorita liike
                            if pelaaja.location["ReqItem"]=="":
                                pelaaja.location=i

                            #Nykyisen sijainnin ja seuraavan huoneen avain sama, testaa onko käytetty.
                            elif pelaaja.location["ReqItem"] == i["ReqItem"]:
                                #Jos on käytetty, suorita liike. Jos pelaaja on peikon huoneessa, varmista että peikko on voitettu
                                if pelaaja.location["ReqItem"] in pelaaja.usedItems:
                                    if pelaaja.location["Name"]=="Syvä luola" and "Miekka" not in pelaaja.usedItems:
                                        #Jos ei, pelaaja häviää
                                        print(pelaaja.location["FailDesc"])
                                        endGame()
                                    else:
                                        pelaaja.location=i
                                else:
                                    #Jos ei, pelaaja häviää
                                    print(pelaaja.location["FailDesc"])
                                    endGame()
                            else:
                                pelaaja.location=i
            else:
                print(f"Et löydä paikkaa {sTarget}.")
        else:
            print("\nSinulla ei ole luita. Olet kykenemätön liikkumana omin voimin.")
            endGame()
        

##Esineet
class Item():
    #Listaus ja käyttö
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
                #Tarkista onko numero inventaarion kantamassa ja käytä
                if 0<=itemUsed<=len(pelaaja.inventory)-1:
                    itemUsed=pelaaja.inventory[itemUsed]
                    #Onko esine huoneen vaatimuksissa
                    if pelaaja.location["ReqItem"]==itemUsed:
                        print(f"Käytät: {itemUsed}.")
                        pelaaja.inventory.remove(itemUsed)
                        pelaaja.usedItems.append(itemUsed)
                    #Käyttääkö pelaaja miekkaa peikkoa vastaan?
                    elif pelaaja.location["Name"]=="Syvä luola" and itemUsed=="Miekka":
                        pelaaja.inventory.remove(itemUsed)
                        pelaaja.usedItems.append(itemUsed)

                    else:
                        print(f"Tämä ei ole oikea paikka esineelle {itemUsed}.")

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

#Pelin päätös
def endGame():
    iScore=0
    for i in pelaaja.inventory:
        iScore=iScore+1
        if i=="Kruunu" or i=="Valtikka":
            iScore=iScore+19
    for i in pelaaja.usedItems:
        iScore=iScore+10
    if bWin==True:
        iScore=iScore*2
        if iScore>=60:
            print("Kreivi Hammark on vakuuttunut suorituksesi, ja palkitsee sinut ylellisellä kartanolla hovin kera!")
        elif iScore>=30:
            print("Saaliisi saa kehut kreivi Hammarkilta, mutta palkkiosi on vaatimaton.")
        else:
            print("Ihmeellistä että edes suoriuduit näin alhaisesti! Yritähän uudelleen!")
    exit(f"Ansaitsit suorituksellasi {iScore} pistettä.")

#Pelaajan alustus
intTest=False
bBones=False
bContinue=False

sName=input("Nimesi: ")
sSavePath=(f"./peliprojekti/save/{sName}.json")

#Kysy tallennuksen jatkamista
if os.path.exists(sSavePath):
    playerInput=input("(J)atka tallennuksesta?\n")
    if str.upper(playerInput)=="J":
        bContinue=True
        with open(sSavePath, "r") as saveFile:
            saveData=json.load(saveFile)
        sName=saveData["sName"]
        iAge=saveData["iAge"]
        bBones=saveData["bBones"]
        location=saveData["location"]
        for i in roomdat.dictRooms:
            if i["Name"]==location:
                location=i
        inventory=saveData["inventory"]
        usedItems=saveData["usedItems"]
        pelaaja=Player(sName, iAge, bBones, location, inventory, usedItems)
        print(f"Tervetuloa takaisin, {pelaaja.sName}!")


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
    playerInput=input("(L)uut?")
    if str.upper(playerInput)=="L":
        bBones=True
    location=roomdat.dictRooms[0]
    pelaaja=Player(sName, iAge, bBones, location)

    #Ikäportti
    if pelaaja.iAge < 12:
        exit(f"Kiitos mielenkiinnostasi {pelaaja.sName}, mutta tämän ohjelman ikäraja on 12.")
    else:
        print(f"\nTerve {pelaaja.sName}! Ikäsi on {pelaaja.iAge}.\n")

##Pääsilumukka
while bRunning == True:
    #Sijainnin nimi ja kuvaus. Jos huoneella on pulma ratkaistavana, testaa onko se suoritettu. Syvä luola on erityistapaus.
    print(f"\n{pelaaja.location["Name"]}")
    if pelaaja.location["ReqItem"]!="" and pelaaja.location["Name"]!="Syvä luola":
        if pelaaja.location["ReqItem"] in pelaaja.usedItems:
            try:
                print(pelaaja.location["SuccDesc"])
            except:
                print(pelaaja.location["Desc"])
        else:
            print(pelaaja.location["Desc"])
    elif pelaaja.location["Name"]=="Syvä luola":
        if "Miekka" in pelaaja.usedItems:
            print(pelaaja.location["SuccDesc"])
        else:
            print(pelaaja.location["Desc"])
    else:
        print(pelaaja.location["Desc"])

    #Aarteet näkyvät listattuna
    if "Kruunu" in pelaaja.location["Items"]:
        print("Ränsistyneen mökin lankkujen välistä kimaltaa kruunu.")
    if "Valtikka" in pelaaja.location["Items"]:
        print("Peikon edellisiltä uhreilta on jäänyt valtiaan valtikka.")

    print("\n1. Liiku\n2. Kerää\n3. Esineet")
    if pelaaja.location["Name"]=="Kartano":
        print("\n(P)alauta löytösi")
    print("tai (L)opeta")
        

    playerInput=input()

    #Liike
    if playerInput=="1":
        Player.move()
    #Inventaario-operaatiot
    if playerInput=="2":
        Item.take()
    if playerInput=="3":
        Item.show()
    if pelaaja.location["Name"]=="Kartano":
        if str.capitalize(playerInput)=="P":
            bWin=True
            endGame()

    #Lopetus
    if str.upper(playerInput)=="L":
        bRunning=False

#Lopetus
playerInput=input("(T)allenna?\n")
if str.upper(playerInput)=="T":
    saveData={
        "sName":pelaaja.sName,
        "iAge":pelaaja.iAge,
        "bBones":pelaaja.bBones,
        "location":pelaaja.location["Name"],
        "inventory":pelaaja.inventory,
        "usedItems":pelaaja.usedItems
    }
    print("\nTallennettu!")
    with open(sSavePath, "w") as saveFile:
        json.dump(saveData, saveFile)

#Pisteiden tulostus tässä
