from Test import Test, Test as test

'''
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,

each taken only once - coming from s1 or s2.
Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
'''

def longest(s1, s2):
    return ''.join(sorted(set(s1 + s2)))

Test.describe("longest")
Test.it("Basic tests")
Test.assert_equals(longest("aretheyhere", "yestheyarehere"), "aehrsty")
Test.assert_equals(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
Test.assert_equals(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")