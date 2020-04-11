from Test import Test

'''
Given an array of ones and zeroes, convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
'''

def binary_array_to_number(arr):
    total = 0
    step = 1
    arr.reverse()
    for digit in arr:
        if digit == 1:
            total += step
        step *= 2
    return total
    


Test.describe("One's and Zero's")
Test.it("Example tests")
Test.assert_equals(binary_array_to_number([0,0,0,1]), 1)
Test.assert_equals(binary_array_to_number([0,0,1,0]), 2)
Test.assert_equals(binary_array_to_number([1,1,1,1]), 15)
Test.assert_equals(binary_array_to_number([0,1,1,0]), 6)
