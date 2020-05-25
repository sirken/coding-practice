from Test import Test, Test as test

'''
Write function avg which calculates average of numbers in given list.
'''

def find_average(arr):
    return sum(arr) / len(arr)

Test.assert_equals(find_average([1, 2, 3]), 2)