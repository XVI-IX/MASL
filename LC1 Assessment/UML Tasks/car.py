from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, passengers, fuelCap,
            fuelCons, make, 
            tDist, tTime, range, gasReq,
            speed, engineType):
        super().__init__( passengers, fuelCap,
            fuelCons, make, 
            tDist, tTime, range, gasReq,
            speed)
        self.engineType = engineType

    def getType(self):
        return self.engineType