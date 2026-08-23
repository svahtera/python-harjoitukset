playerName=input("Nimesi:\n")
numTest=False
while numTest==False:
    playerAge=input("ikäsi: ")
    try:
        int(playerAge)
    except:
        print("Ikä voi olla vain kokonaisluku.")
    else:
        playerAge=int(playerAge)
        numTest=True

if playerAge < 12:
    print(f"Kiitos mielenkiinnostasi, {playerAge}, mutta tämän ohjelman ikäraja on 12.")
    exit()
else:
    print(f"Terve {playerAge}! Ikäsi on {playerAge}.")