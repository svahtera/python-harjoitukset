import math
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

#Autojen generointi
for i in range(10):
    sLicense="ABC-"+str(i+1)
    iGenSpeed=int(random.randint(100,200))
    lCars.append(Auto(sLicense, iGenSpeed))

#Ajo
#while bFinish!=True:
#    for r in lCars:
#        r.accelerate(random.randint(-10, 15))
#        fTime=fTime+1
#        r.drive(fTime)
#        if r.iDistance>=10000:
#            bFinish=True
#
#print(f"\tHuippu- \tNopeus \tKuljettu:")
#print(f"Auto: \tnopeus: \tNyt \tMatka:")
#
#for i in lCars:
#    i.report()


#Ajo
race1=Race("Suuri romuralli", 8000, lCars)
iTime=0
bFinish=False
while bFinish!=True:
    iTime=iTime+1
    race1.hourly()
    bFinish=race1.finish()
    if iTime==10:
        iTime=0
        race1.standings()
race1.standings()