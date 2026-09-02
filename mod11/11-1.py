#Julkaisuluokka
class Publication:
    def __init__(self, name):
        self.name=name

    def printInfo(self):
        print(self.name)

#Kirjaluokka
class Book(Publication):
    def __init__(self, name, author, pages):
        self.author=author
        self.pages=pages
        super().__init__(name)

    def printInfo(self):
        super().printInfo()
        print(f"{self.author}, {self.pages} sivua\n")

#Lehtiluokka
class Magazine(Publication):
    def __init__(self, name, edInChief):
        self.edInChief = edInChief
        super().__init__(name)

    def printInfo(self):
        super().printInfo()
        print(f"{self.edInChief}\n")

lPublications=[]
lPublications.append(Magazine("Aku Ankka", "Aki Hyyppä"))
lPublications.append(Book("Hytti N:o 6", "Rosa Liksom", 200))

for i in lPublications:
    i.printInfo()