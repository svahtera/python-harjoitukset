n=int(input("Syötä kokonaisluku: "))

comp=False

#Vain parittomat luvut voivat olla alkulukuja
#Ohjelmaa on turha jatkaa kun on testannut yli puolet luvun suuruudesta
for i in range(1,int(n/2+1),2):

    #Annettuluku on yhdistetty luku jos siitä ei jää jakojäännöstä
    if n/(i+1)==int(n/(i+1)):
        if i+1!=1:
            comp=True
            break
if comp==True:
    print(f'{n}{" ei ole alkuluku"}')
else:
    print(f'{n}{" on alkuluku"}')