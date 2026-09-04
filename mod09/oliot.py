class Koira:

    tehty=0
    vari="blank"

    def __init__(self, nimi, syntymavuosi, vari, bark="Vuh-vuh"):
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi
        self.bark=bark
        self.vari=vari
        Koira.vari=vari
        Koira.tehty=Koira.tehty + 1

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.bark)

koirat=[]

koira1=Koira("Muro", 2018, "musta")
print(Koira.vari)
koira2=Koira("Rekku", 2018, "ruskea", "Viu viu viu")
print(Koira.vari)

print(f"Koiria on nyt {Koira.tehty}.")
#print(f"Edellisen koiran väri on {Koira.vari}.")
#svuosi=2016
#nimi="a"

#for i in range(10):
#    koirat.append(Koira(nimi, svuosi))
#    svuosi+=1
#    nimi=chr(ord(nimi)+1)
#for i in koirat:
#    print(i.nimi, i.syntymavuosi)