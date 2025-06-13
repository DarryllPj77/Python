from abc import ABC, abstractmethod
class Car(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
 
    @abstractmethod
    def start(self):
      pass
 
    @abstractmethod
    def stop(self):
      pass
 
    @abstractmethod
    def run(self):
      pass
 
    @abstractmethod
    def accelerate(self):
      pass
 
class SportsCar(Car):
      def __init__(self, make, model, year):
        super().__init__(make, model, year)  
 
      #Abstraction
      def start(self):
        print("Starting the sports_car...")
 
      def stop(self):
        print("Stopping the sports_car...")
 
      def run(self):
        print("Running...")
 
      def accelerate(self):
        print("Accelerating...")
 
 
yungRed = SportsCar('Lamborghini', 'Aventador', 2023)
yungRed.start()
yungRed.stop()
yungRed.run()
yungRed.accelerate()
