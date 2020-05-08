from Test import Test, Test as test

'''
Convert number to reversed array of digits
Given a random number:

C#: long;
C++: unsigned long;
You have to return the digits of this number within an array in reverse order.

Example:
348597 => [7,9,5,8,4,3]
'''

# Mine
def digitize(n):
    return list(int(i) for i in reversed(str(n)))

# Using map, looping reverse. Fails in PyCharm, apparently works in Codewars
def digitize(n):
    return map(int, str(n)[::-1])

# Looping reverse
def digitize(n):
    return [int(x) for x in str(n)[::-1]]

Test.assert_equals(digitize(35231),[1,3,2,5,3])