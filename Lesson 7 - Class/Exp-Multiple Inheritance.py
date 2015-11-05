__author__ = 'MinhDuc'
import random

class People():
    def __init__(self, eyecolor, skincolor, haircolor, country = 'people'):
        self.eyecolor = eyecolor
        self.skincolor = skincolor
        self.haircolor = haircolor
        self.country = country

    def __str__(self):
        return ('%s has %s eye, %s skin and %s hair.' % (self.country, self.eyecolor, self.skincolor, self.haircolor))


class AsiaPeople(People):
    def GoodAtMath(self):
        print('%s good at math' % self.country)


class EuroPeople(People):
    def GoodAtSport(self):
        print('%s good Art and Sport' % self.country)


class AsiaEuroPeople(AsiaPeople, EuroPeople):
    def __init__(self, mothercountry, fathercountry):
        self.country = ('%s - %s' % (mothercountry, fathercountry))
        self.eyecolor = random.choice(['black', 'blue', 'dark blue'])
        self.skincolor = random.choice(['white', 'white', 'pink'])
        self.haircolor = random.choice(['black', 'blond', 'red'])

japanness = AsiaPeople('black', 'yellow', 'black', 'Janpaness')
print(japanness)
print()
Swedish = EuroPeople('blue', 'white', 'blond', 'Swenden')
print(Swedish)
print()
japanSwed = AsiaEuroPeople('Japanness', 'Sweden')
print(japanSwed)
print()
japanSwed.GoodAtMath()
japanSwed.GoodAtSport()
