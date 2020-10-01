from Test import Test, Test as test

'''
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
'''

# Use ord()
def alphabet_position(text):
    out = []
    for x in text:
        val = ord(x.upper())-64
        if 27 > val > 0:
            out.append(str(val))
    return ' '.join(out)

# Condensed
def alphabet_position(text):
    return ' '.join(str(ord(x.upper())-64) for x in text if 27 > ord(x.upper())-64 > 0)



test.assert_equals(alphabet_position("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
test.assert_equals(alphabet_position("The narwhal bacons at midnight."), "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")