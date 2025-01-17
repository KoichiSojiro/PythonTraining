'''
Created on Jul 26, 2016

@author: trannh08
'''
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        print("This is a " + str(self.color) + " " + str(self.model) + " with " + str(self.mpg) + " MPG.")
    def drive_car(self):
        self.condition = "used"

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        super(ElectricCar, self).__init__(model, color, mpg)
        self.battery_type = battery_type
    def display_car(self):
        inherit_Str = super(ElectricCar, self).display_car()
        return(inherit_Str + "It has a %s battery. " % (self.battery_type))
    def drive_car(self):
        self.condition = "like new"

my_car = ElectricCar("Watch Dog", "Black", 199, "molten salt")
print(my_car.condition)
my_car.drive_car()
print(my_car.condition)