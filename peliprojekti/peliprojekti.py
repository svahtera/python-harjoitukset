#Luvunsyöttöfunktio
def numIn(sQuery, sError="Luku ei kelpaa. Syötä vain numeroita."):
    t=False
    while t==False:
        num=input(sQuery)
        num=num.replace(",", ".")
        try:
            float(num)
        except:
            print(sError)
        else:
            num=float(num)
            t=True
    return num

def invMod(sName, iCount):

    pass

lInventory = [
    {
        "item":"",
        "count":"0"
    },
    {
        "item":"",
        "count":"0"
    },
    {
        "item":"",
        "count":"0"
    }
]

playerName=input("Nimesi: ")
playerAge=int(numIn("Ikäsi: ","Ikä voi olla vain kokonaisluku."))

if playerAge < 12:
    print(f"Kiitos mielenkiinnostasi {playerName}, mutta tämän ohjelman ikäraja on 12.")
    exit()
else:
    print(f"Terve {playerName}! Ikäsi on {playerAge}.")

print("Mitä kannat?")
