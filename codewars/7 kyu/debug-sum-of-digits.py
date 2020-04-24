from Test import Test, Test as test

'''
Debug   function getSumOfDigits that takes positive integer to calculate sum of it's digits. Assume that argument is an integer.

Example
123  => 6
223  => 7
1337 => 15
'''

def get_sum_of_digits(num):
    return sum([int(x) for x in str(num)])

def get_sum_of_digits(num):
    return sum([x for x in map(int, str(num))])

def get_sum_of_digits(num):
    return sum(map(int, str(num)))

test.assert_equals(get_sum_of_digits(123), 6)