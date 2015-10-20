__author__ = 'MinhDuc'

class Type:
    def __init__(self, name, func, typeStreet):
        self.name = name
        self.func = func
        self.typeStreet = typeStreet

    def __str__(self):
        return '%s can %s on %s.' % (self.name, self.func, self.typeStreet)

class Car(Type):
    def __init__(self):
        Type.__init__(self, 'car', 'run', 'road')

class Canoe(Type):
    def __init__(self):
        Type.__init__(self, 'canoe', 'sufring', 'riverway')

class Amphibian(Car,Canoe):
    def __init__(self, type1, type2):
        self.name = '%s_%s' % (type1, type2)
        self.func = 'run and surfing'
        self.typeStreet = 'road and riverway'

car = Car()
print(car)
print()
canoe = Canoe()
print(canoe)
print()
amphilican = Amphibian('car', 'canoe')
print(amphilican)
