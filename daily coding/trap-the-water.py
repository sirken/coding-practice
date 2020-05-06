from Test import Test
'''
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
'''

# Some ideas
# 1. Find all peaks
# 1a. Save as sub-lists
# 2. Fill in water


def check_answer(arr):
    high_start = arr[0]
    high_end = 0
    in_valley = False
    
    peaks = []

    for i in arr[1:]:
        # New start
        if i > high_start:
            high_start = i
            pass
        elif i < high_start:
            pass
        total += i - min_val
    return total



Test.assert_equals(check_answer([3, 0, 1, 3, 0, 5]), 8)