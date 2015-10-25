__author__ = 'MinhDuc'
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getarea(self):
        return self.radius ** 2 * math.pi

    def getprimeter(self):
        return self.radius * 2 * math.pi

circle1 = Circle(20)
circle2 = Circle(10)

print('Radius: ', circle1.radius, ' | Area: ', circle1.getarea(), ' | Primeter: ', circle1.getprimeter())
print('Radius: ', circle2.radius, ' | Area: ', circle2.getarea(), ' | Primeter: ', circle2.getprimeter())
