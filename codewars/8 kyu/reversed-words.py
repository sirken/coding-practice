from Test import Test, Test as test

'''
Complete the solution so that it reverses all of the words within the string passed in.
'''

def reverse_words(s):
    return ' '.join(reversed(s.split(' ')))

test.assert_equals(reverse_words("hello world!"), "world! hello")