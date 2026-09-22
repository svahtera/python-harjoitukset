number=int(input("Syötä kokonaisluku: "))

comp=False

#Vain parittomat luvut voivat olla alkulukuja
#Ohjelmaa on turha jatkaa kun on testannut yli puolet luvun suuruudesta
for i in range(3,int(number/2+1),2):
    #Annettuluku on yhdistetty luku jos siitä ei jää jakojäännöstä
    if number % i == 0:
        comp=True
        break
if number == 1:
    comp=True
if comp==True:
    print(f'{number}{" ei ole alkuluku"}')
else:
    print(f'{number}{" on alkuluku"}')