username="python"
password="rules"

for i in range(5):
    usernameIn=input("Käyttäjänimi: ")
    passwordIn=input("Salasana: ")
    if usernameIn==usernameIn and passwordIn==password:
        print("Tervetuloa")
        exit()
    if i==4:
        print("Pääsy evätty")