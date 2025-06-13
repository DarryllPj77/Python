class Shape:
    size = 1 #Class Attribute (static)
    def __init__(self, color):
        self.__color = color #Instance Attribute
 
    #getter and setter
    def get_color(self):
        return self.__color
 
    def set_color(self, color):
        self.__color = color
class Shape:
    size = 1 #Class Attribute (static)
    def __init__(self, color):
        self.__color = color #Instance Attribute
 
    #getter and setter
    def get_color(self):
        return self.__color
 
    def set_color(self, color):
        self.__color = color
 
circle = Shape('red')
print("Color:", circle.get_color())
print("Size:", circle.size)
 
star = Shape('yellow')
star.set_color("Dark Blue")
print("Color:", star.get_color())
print("Size:", star.size)
circle = Shape('red')
print("Color:", circle.get_color())
print("Size:", circle.size)
 
star = Shape('yellow')
star.set_color("Dark Blue")
print("Color:", star.get_color())
print("Size:", star.size)
