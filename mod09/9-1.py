import math
import random

fTime=0
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
    def drive(self, fTime):
        self.iDistance=int(math.fma(fTime, self.iCurSpeed, self.iDistance))
        return self.iDistance>=10000


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
    for r in lCars:
        r.accelerate(random.randint(-10, 15))
        fTime=fTime+1
        r.drive(fTime)
        if r.iDistance>=10000:
            bFinish=True

print(f"\tHuippu- \tNopeus \tKuljettu:")
print(f"Auto: \tnopeus: \tNyt \tMatka:")

for i in lCars:
    i.report()