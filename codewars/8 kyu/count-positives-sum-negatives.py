from Test import Test, Test as test

'''
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
'''

def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    l = [0,0]
    for i in arr:
        if i > 0:
            l[0] += 1
        else:
            l[1] += i
    return l

# Other similar
def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [pos, neg]

# Other different, nice
def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []

Test.describe("Basic tests")
Test.assert_equals(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]),[10,-65])
Test.assert_equals(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]),[8,-50])
Test.assert_equals(count_positives_sum_negatives([1]),[1,0])
Test.assert_equals(count_positives_sum_negatives([-1]),[0,-1])
Test.assert_equals(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]),[0,0])
Test.assert_equals(count_positives_sum_negatives([]),[])