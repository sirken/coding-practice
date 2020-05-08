from Test import Test, Test as test

'''
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
'''

# Store in nested lists
# When both lists have items and one has more than 1
def find_outlier(integers):
    l = [[],[]]
    for i in integers:
        if i % 2 == 0:
            l[0].append(i)
        else:
            l[1].append(i)
        if len(l[1]) > 1 and len(l[0]) == 1:
            return l[0][0]
        elif len(l[0]) > 1 and len(l[1]) == 1:
            return l[1][0]


test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)