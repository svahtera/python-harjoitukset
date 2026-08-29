#Hissit
class Elevator:
    def __init__(self, iBottom, iTop):
        self.iBottom=iBottom
        self.iTop=iTop
        self.iCurrent=iBottom

    #Sirry kerrokseen
    def moveTo(self, iTarget, iElevatorId):
        while self.iCurrent>iTarget:
            self.moveDown(iElevatorId)
        while self.iCurrent<iTarget:
            self.moveUp(iElevatorId)
        return

    #Siirry alas
    def moveUp(self, iElevatorId):
        self.iCurrent=self.iCurrent+1
        print(f"Hissi {iElevatorId} on {self.iCurrent}. kerroksessa.")
        return

    #Siirry Ylös
    def moveDown(self, iElevatorId):
        self.iCurrent=self.iCurrent-1
        print(f"Hissi {iElevatorId} on {self.iCurrent}. kerroksessa.")
        return

#Talo
class House:
    def __init__(self, iBottom, iTop, iElevators):
        self.iBottom=iBottom
        self.iTop=iTop
        self.lElevators=[]
        for i in range(iElevators):
            self.lElevators.append(Elevator(iBottom, iTop))

    #Aja hissiä
    def driveElevator(self, iElevatorId, iTarget):
        self.iElevatorId=iElevatorId
        self.iTarget=iTarget
        self.lElevators[iElevatorId].moveTo(self.iTarget, iElevatorId)
        return

    #Palohälytys
    def fireAlarm(self):
        r=0
        print("Palohälytys!")
        for i in self.lElevators:
            self.driveElevator(r, self.iBottom)
            r=r+1
        return

house1=House(0, 10, 2)
house1.driveElevator(0, 5)
house1.driveElevator(1, 3)
house1.fireAlarm()