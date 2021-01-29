from Test import Test, Test as test

'''
In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.

For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.

Your function will be tested with pre-made examples as well as random ones.

If you can, try writing it in one line of code.
'''

def prod_list(list):
    prod = 1
    for num in list:
        prod *= num
    return prod

def find_difference(a, b):
    return abs(prod_list(a) - prod_list(b))


# Top solution
from numpy import prod

def find_difference(a, b):
    return abs(prod(a) - prod(b))


test.assert_equals(find_difference([3, 2, 5], [1, 4, 4]), 14, "{0} should equal 14".format(find_difference([3, 2, 5], [1, 4, 4])))
test.assert_equals(find_difference([9, 7, 2], [5, 2, 2]), 106, "{0} should equal 106".format(find_difference([9, 7, 2], [5, 2, 2])))