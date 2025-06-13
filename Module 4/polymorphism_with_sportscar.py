class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
 
    def start(self):
      print("Starting the car...")
 
    def stop(self):
      print("Stopping the car...")
 
class SportsCar(Car):
      def __init__(self, make, model, year):
        super().__init__(make, model, year)  
 
      #Polymorphism (Overridding)
      def start(self):
        print("Starting the sports_car...")
 
      def stop(self):
        print("Stopping the sports_car...")
 
yungRed = SportsCar('Lamborghini', 'Aventador', 2023)
yungRed.start()
yungRed.stop()
