
class vehicle:

    def __init__(self,brand,model,year,speed):
        print("in vehicle constructor")
        self.brand = brand 
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        print("in accelerate method: vehicle")
        print(self.speed)

    def brake(self):
        print("in brake method: vehicle")
        print("brake is activated speed is decresing")

    def honk(self):
        print("in honk method: vehicle")
        print("horn is activate pooooooooooooopooooooooooo")

class ch_vehicle(vehicle):

    def __init__(self):
        print("in child vehicle constructor ")

    def accelerate(self):
        print("in  accelerate method: child vehicle")

    def honk(self):
        print("in hok method: child vehicle")


brand = input("enter the brand of the vehicle:")
model = input("enter the model of the vehicle:")
year = input("enter the year of the vehicle:")
speed = input("enter the speed of the vehicle:")
        
if __name__=="__main__":
    obj1 = vehicle(brand,model,year,speed)
    obj2 = ch_vehicle()
    obj1.accelerate()
    obj2.accelerate()
    obj1.brake()
    obj2.brake()
    obj1.honk()
    obj2.honk()

