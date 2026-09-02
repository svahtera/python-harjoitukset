import random

lCars=[]
bFinish=False

##Autoluokka
class Auto:
    def __init__(self, sLicense, iTopSpeed, iCurSpeed=0, iDistance=0):
        self.sLicense=sLicense
        self.iTopSpeed=iTopSpeed
        self.iCurSpeed=iCurSpeed
        self.iDistance=iDistance

    #Kiihdytys
    def accelerate(self, iAcc):
        iTargetSpeed=self.iCurSpeed+iAcc
        if iTargetSpeed >= self.iTopSpeed:
            self.iCurSpeed=iTargetSpeed
        elif iTargetSpeed <= 0:
            self.iCurSpeed=0
        else:
            self.iCurSpeed=self.iCurSpeed+iAcc

    #Ajometodi
    def drive(self):
        self.iDistance=self.iDistance+self.iCurSpeed
        return


    #raportointi
    def report(self):
        print(f"{self.sLicense:<10}{str(self.iTopSpeed)+' km/h':<12}{str(self.iCurSpeed)+' km/h':12}{str(self.iDistance)+' km'}")

##Kilpailuluokka
class Race:
    def __init__(self, sName, iLength, lCars):
        self.sName=sName
        self.iLength=iLength
        self.lCars=lCars

    #Joka tunti
    def hourly (self):
        for i in self.lCars:
            i.accelerate(random.randint(-10, 15))
            i.drive()
        return

    #tilanne
    def standings(self):
        print(f"{'':<10}{'Huippu-':<12}{'Nopeus':<12}{'Kuljettu'}")
        print(f"{'Auto:':<10}{'nopeus:':<12}{'Nyt':<12}{'Matka:'}")
        for i in lCars:
            i.report()
        return

    #Maali
    def finish (self):
        for i in lCars:
            if i.iDistance>=self.iLength:
                bFinish=True
                break
            else:
                bFinish=False
        return bFinish

#Sähkö- ja polttomottootorit
class Electric(Auto):
    def __init__(self, sLicense, fBattCap, iTopSpeed):
        self.battCap=fBattCap
        Auto.__init__(self, sLicense, iTopSpeed)

class Gas(Auto):
    def __init__(self, sLicense, fFuelCap, iTopSpeed):
        self.fuelCap=fFuelCap
        Auto.__init__(self, sLicense, iTopSpeed)

#Autojen määrittely
lCars.append(Electric("ELV-015", 52.5, 180))
lCars.append(Gas("GAS-123", 32.3, 165))


#Ajo
for i in range(3):
    for i in lCars:
        i.accelerate(20)
        i.drive()

print(f"{'':<10}{'Huippu-':<12}{'Nopeus':<12}{'Kuljettu'}")
print(f"{'Auto:':<10}{'nopeus:':<12}{'Nyt':<12}{'Matka:'}")
for i in lCars:
    i.report()