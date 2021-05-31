from Test import Test, Test as test

'''
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
'''

def bmi(weight, height):
    b = weight / height ** 2
    p = "Slim"
    if b > 30:      p = "Obese"
    elif b > 25:    p = "Overweight"
    elif b > 18.5:  p = "Normal"
    else:           p = "Underweight"
    return p

test.assert_equals(bmi(50, 1.80), "Underweight")
test.assert_equals(bmi(80, 1.80), "Normal")
test.assert_equals(bmi(90, 1.80), "Overweight")
test.assert_equals(bmi(110, 1.80), "Obese")
test.assert_equals(bmi(50, 1.50), "Normal")