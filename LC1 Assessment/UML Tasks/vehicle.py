class Vehicle:
    def __init__(
            self, passengers,
            fuelCap, fuelCons,
            make, tDist, tTime,
            range, gasReq, speed
        ):
        
        self.passengers = passengers
        self.fuelCap = fuelCap
        self.fuelCons = fuelCons
        self.make = make
        self.tDist = tDist
        self.tTime = tTime
        self.range = range
        self.gasReq = gasReq
        self.speed = speed

    def findGasNeeded(self):
        gas = self.fuelCap - self.fuelCons
        return gas
    
    def getSpeed(self):
        return self.speed
    
    def findSpeed(self, tTime, tDist):
        speed = tDist / tTime
        return speed
    
    def findRange(self, fuelGiven):
        rangeRate = self.tDist / self.fuelCap
        return rangeRate * fuelGiven
