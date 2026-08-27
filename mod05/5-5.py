username="python"
password="rules"

for i in range(5):
    usernameIn=input("Käyttäjänimi: ")
    passwordIn=input("Salasana: ")
    if usernameIn==usernameIn and passwordIn==password:
        break
    elif i==4:
        exit("Pääsy Evätty")
print("Tervetuloa")