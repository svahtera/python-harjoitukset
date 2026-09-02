username="python"
password="rules"

bLogin=False
iAttempts=0
while bLogin==False:
    usernameIn=input("Käyttäjänimi: ")
    passwordIn=input("Salasana: ")
    if usernameIn==username and passwordIn==password:
        bLogin=True
    else:
        iAttempts=iAttempts+1
        if iAttempts==5:
            exit("Pääsy Evätty")
print("Tervetuloa")