from Test import Test, Test as test

'''
Your task is to make two functions, max and min (maximum and minimum in PHP and Python, maxi and mini in Julia) that take a(n) array/vector of integers list as input and outputs, respectively, the largest and lowest number in that array/vector.

#Examples

maximun([4,6,2,1,9,63,-134,566]) returns 566
minimun([-52, 56, 30, 29, -54, 0, -110]) returns -110
maximun([5]) returns 5
minimun([42, 54, 65, 87, 0]) returns 0
'''

def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

test.assert_equals(minimum([-52, 56, 30, 29, -54, 0, -110]), -110)
test.assert_equals(minimum([42, 54, 65, 87, 0]), 0)
test.assert_equals(minimum([1, 2, 3, 4, 5, 10]), 1)
test.assert_equals(minimum([-1, -2, -3, -4, -5, -10]), -10)
test.assert_equals(minimum([9]), 9)

test.assert_equals(maximum([-52, 56, 30, 29, -54, 0, -110]), 56)
test.assert_equals(maximum([4, 6, 2, 1, 9, 63, -134, 566]), 566)
test.assert_equals(maximum([5]), 5)
test.assert_equals(maximum([534, 43, 2, 1, 3, 4, 5, 5, 443, 443, 555, 555]), 555)
test.assert_equals(maximum([9]), 9)