class BMI:

    def __init__(self, name, weight, height, *age):
        self.name = name
        self.weight = weight
        self.height = height
        if len(age) == 0:
            self.age = 20
        else:
            self.age = age


    def getBMI(self):
        return (self.weight * 0.45) / ((self.height * 0.0254) ** 2 )

    def getStatus(self):
        if self.getBMI() < 18.5:
            return 'Underweight'
        elif self.getBMI() < 25:
            return 'Normal'
        elif self.getBMI() < 30:
            return 'underweight'
        else:
            return 'Obese'

    def getName(self):
        return self.name

    def checkName(self):
        print ('Name:', self.name, ', age: ', self.age, ', weight:', self.weight, ', height: ', self.height)

class UseGetBMI(BMI):
    bmi1 = BMI('Kim Yang', 145, 70, 18)
    print('The BMI for', bmi1.getName(), ' is ', ':.2f'.format(bmi1.getBMI()) , ' ', bmi1.getStatus())
    bmi1.checkName()
    bmi2 = BMI('Susan King', 215, 70)
    print('The BMI for', bmi2.getName(), ' is ', bmi2.getBMI(), ' ', bmi2.getStatus())
    bmi2.checkName()