from Test import Test, Test as test

'''
Will you make it?
You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel 
is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles 
per gallon. There are 2 gallons left. Considering these factors, write a function that tells you if it is possible 
to get to the pump or not. Function should return true (1 in Prolog) if it is possible and false (0 in Prolog) if 
not. The input values are always positive.
'''

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump



test.assert_equals(zero_fuel(50, 25, 2), True)
test.assert_equals(zero_fuel(100, 50, 1), False)