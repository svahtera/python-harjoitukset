playerInput=""

playerName=input("Nimesi: ")
playerAge=int(input("Ikäsi: "))

if playerAge < 12:
    print(f"Kiitos mielenkiinnostasi {playerName}, mutta tämän ohjelman ikäraja on 12.")
else:
    print(f"Terve {playerName}! Ikäsi on {playerAge}.\n")

#mainMenu
while str.upper(playerInput)!="1":
    print("\nHIENO OTSIKKO\n")
    print(f"1. Aloita\n2. Epäsulje hypervalikko\n3. Siisteydentunnistus\n4. Luut\n\ntai LOPETA")   #Valikoiden status puuttuu
    playerInput=input()
    if playerInput=="2":
        print("Hypervalikko epäsuljettu.")
    if playerInput=="3":
        print("Siisteyden tunnistus aktivoitu.")
    if playerInput=="4":
        print("Luut pois päältä.")
    if str.upper(playerInput)=="LOPETA":
        exit("Kiitos käynnistä")
print("Ei implementoitu")