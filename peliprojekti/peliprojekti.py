playerInput=""

playerName=input("Nimesi: ")
playerAge=int(input("Ikäsi: "))

if playerAge < 12:
    print(f"Kiitos mielenkiinnostasi {playerName}, mutta tämän ohjelman ikäraja on 12.")
else:
    print(f"Terve {playerName}! Ikäsi on {playerAge}.\n")

#mainMenu
while str.upper(playerInput)!="LOPETA":
    print("HIENO OTSIKKO\n")
    print(f"1. Aloita\n2. Epäsulje hypervalikko\n3. Siisteydentunnistus\n tai LOPETA")   #Valikoiden status puuttuu
    playerInput=input("")
    if playerInput==1:
        break
    if playerInput==2:
        print("Hypervalikko epäsuljettu.")
    if playerInput==3:
        print("Siisteyden tunnistus aktivoitu")
print("Ei implementoitu")