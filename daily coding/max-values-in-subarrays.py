from Test import Test, Test as test

'''
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
'''

# Find length of array, minus k so we don't go too far
def sub_array(arr, k):
    l = len(arr)
    sub = []
    for pos, x in enumerate(range(l-k+1)):
        print(arr[pos:pos+k])
        sub.append(max(arr[pos:pos+k]))
    return sub

# Simplified
def sub_array(arr, k):
    return [max(arr[pos:pos+k]) for pos, x in enumerate(range(len(arr)-k+1))]


test.assert_equals(sub_array([10,5,2,7,8,7], 1), [10,5,2,7,8,7])
test.assert_equals(sub_array([10,5,2,7,8,7], 2), [10,5,7,8,8])
test.assert_equals(sub_array([10,5,2,7,8,7], 3), [10,7,8,8])
test.assert_equals(sub_array([10,5,2,7,8,7], 4), [10,8,8])
test.assert_equals(sub_array([10,5,2,7,8,7], 5), [10,8])
test.assert_equals(sub_array([10,5,2,7,8,7], 6), [10])
