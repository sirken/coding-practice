from Test import Test

'''
Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
'''

# My solution
def get_middle(s):
    while len(s) > 2:
        s = s[1:-1]
    return s

# Shorter, harder to read
# First half: use math that slices at same spot regardless of odd/even
# Second half: add one
def get_middle(s):
    return s[(len(s)-1)//2:len(s)//2+1]


Test.assert_equals(get_middle("test"),"es")
Test.assert_equals(get_middle("testing"),"t")
Test.assert_equals(get_middle("middle"),"dd")
Test.assert_equals(get_middle("A"),"A")
Test.assert_equals(get_middle("of"),"of")
