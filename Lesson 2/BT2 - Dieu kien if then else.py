height = 68
weight = 120
BMI = (weight*0.45359237)/((height*0.0254)*(height*0.0254))
if  BMI < 18.5:
    print('underweight')
elif BMI < 25:
    print('normal')
elif BMI < 30:
    print('overweight')
else:
    print('obese')