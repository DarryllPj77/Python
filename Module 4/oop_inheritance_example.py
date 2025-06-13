class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
 
        # Method to display car information
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")
 
#Inheritance
      #Child     (Parent)
      #Subclass  (Superclass)
  #Derived Class (Based Class)
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size
 
ev = ElectricCar('Tesla', 'Model S', 2025, 100)
ev.display_info()
print("Battery Size:", ev.battery_size)
