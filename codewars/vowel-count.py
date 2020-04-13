from Test import Test, Test as test

'''
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.
'''

# Submitted
def getCount(inputStr):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return sum([inputStr.count(v) for v in vowels])

# Facepalm
def getCount(inputStr):
    return sum([inputStr.count(v) for v in ['a', 'e', 'i', 'o', 'u']])

# Top rated
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

test.assert_equals(getCount("abracadabra"), 5)
