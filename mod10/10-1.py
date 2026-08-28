iTargetFloor=0

class Elevator:
    def __init__(self, iBottom, iTop):
        self.iBottom=iBottom
        self.iTop=iTop
        self.iCurrent=iBottom

    def moveTo(self, iTarget):
        if iTarget>=self.iBottom:
            self.moveDown()
        if iTarget<=self.iTop:
            self.moveUp()

    def moveUp(self, iCurrent, iTop):
        self.iCurrent=self.iCurrent+1
        print(f"Hissi on {self.iCurrentFloor}. kerroksessa.")

    def moveDown(self, iCurrent, iBottom):
        self.iCurrent=self.iCurrent-1
        print(f"Hissi on {self.iCurrentFloor}. kerroksessa.")

 