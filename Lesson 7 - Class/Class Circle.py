__author__ = 'MinhDuc'
import math
class Circle:
    radius = 1

    @staticmethod
    def setradius(newradius):
        Circle.radius = newradius

    @staticmethod
    def getarea():
        return Circle.radius ** 2 * math.pi

    @staticmethod
    def getprimeter():
        return Circle.radius * 2 * math.pi

Circle.setradius(5)

print('Radius:', Circle.radius, ', Area: ', Circle.getarea(), ', Primeter: ', Circle.getprimeter())