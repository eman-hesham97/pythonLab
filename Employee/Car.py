class Car:
    def __init__(self, name, fuelRate, velocity):
        self.carName = name
        self.fuelRate = fuelRate
        self.velocity = velocity
        if self.velocity<0 and self.velocity>200:
            print("Velocity is a value between 0 and 200")
        if self.fuelRate<0 and self.fuelRate>100:
            print("Fuel rate is a value between 0 and 100")

    def run(self, velocity, distance):
        self.velocity = velocity
        while(distance > 0 and self.fuelRate > 0):
                distance -= 1
        remainingDistance = distance
        self.stop(remainingDistance)

    def stop(self, remainingDistance):
        if remainingDistance > 0:
            print(f"remaining distance is: " + {remainingDistance})
        else:
            print("Arrived to destination")