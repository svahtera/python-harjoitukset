import math
import random

lCars=[]
bFinish=False

#Autoluokka
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
        self.iDistance=self.iCurSpeed+self.iDistance
        return


    #raportointi
    def report(self):
        print(f"{self.sLicense} \t{self.iTopSpeed}km/h \t{self.iCurSpeed}km/h \t{self.iDistance}km")

#Autojen generointi
for i in range(10):
    sLicense="ABC-"+str(i+1)
    iGenSpeed=int(random.randint(100,200))
    lCars.append(Auto(sLicense, iGenSpeed))

#Ajo
while bFinish!=True:
    for i in lCars:
        i.accelerate(random.randint(-10, 15))
        i.drive()
        if i.iDistance>=10000:
            bFinish=True

print(f"\tHuippu- \tNopeus \tKuljettu:")
print(f"Auto: \tnopeus: \tNyt \tMatka:")

for i in lCars:
    i.report()