from Test import Test, Test as test

'''
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.
'''

def add_binary(a,b):
    return str(bin(a+b))[2:]

# Str not needed
def add_binary(a,b):
    return bin(a+b)[2:]

Test.assert_equals(add_binary(1, 1), "10")
Test.assert_equals(add_binary(0, 1), "1")
Test.assert_equals(add_binary(1, 0), "1")
Test.assert_equals(add_binary(2, 2), "100")
Test.assert_equals(add_binary(51, 12), "111111")