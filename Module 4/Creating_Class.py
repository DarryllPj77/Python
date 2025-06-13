#Python
 
class Animal: #PascalCase
    #Attributes (Variables)
    age = 1
    gender = 'male'
 
    #Bevahiors (Functions/Methods)
    def __init__(self, name):
        self.name = name
 
    def sound(self, sound):
        print("Sound:", sound)
 
dog = Animal('Snoppy') # dog is an object and Animal is a class
print("Name: ", dog.name)
dog.sound('woof')
 
cat = Animal('Garfield')
print("Name: ", cat.name)
cat.sound('meow')
