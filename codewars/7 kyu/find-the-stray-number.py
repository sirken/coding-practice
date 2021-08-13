from Test import Test, Test as test

'''
You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3
'''

def stray(arr):
    return [x for x in arr if arr.count(x) == 1][0]



test.assert_equals(stray([1, 1, 1, 1, 1, 1, 2]), 2)
test.assert_equals(stray([2, 3, 2, 2, 2]), 3)
test.assert_equals(stray([3, 2, 2, 2, 2]), 3)