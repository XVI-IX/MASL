from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(
            self, wheels, cargoSpace,
            passengers, fuelCap,
            fuelCons, make, 
            tDist, tTime, range, gasReq,
            speed
            ):
        Vehicle.__init__(
            passengers, fuelCap,
            fuelCons, make, 
            tDist, tTime, range, gasReq,
            speed)
        self.wheels = wheels
        self.cargoSpace = cargoSpace

    def getNumWheels(self):
        return self.wheels
    
    def setCargoSpace(self, space):
        self.cargoSpace = space

    def setNumWheels(self, wheels):
        self.wheels = wheels

if __name__ == "__main__":
    daewoo = Truck()