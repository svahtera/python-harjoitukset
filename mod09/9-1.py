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
        print(f"{self.sLicense:<10}{str(self.iTopSpeed)+' km/h':<12}{str(self.iCurSpeed)+' km/h':12}{str(self.iDistance)+' km'}")


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

print(f"{'':<10}{'Huippu-':<12}{'Nopeus':<12}{'Kuljettu'}")
print(f"{'Auto:':<10}{'nopeus:':<12}{'Nyt':<12}{'Matka:'}")

for i in lCars:
    i.report()