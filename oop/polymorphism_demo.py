# a simple script to demonstrate  ,method overriding and polymorphic behavior
import math

class Shape:
    def area(self):
        raise NotImplementedError("A derived class needs to override this!")
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2
    