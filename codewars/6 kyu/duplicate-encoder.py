from Test import Test

'''
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
'''

def duplicate_encode(word):
    o = ''
    for l in word:
        if word.lower().count(l.lower()) == 1:
            o = o + '('
        else:
            o = o + ')'
    return o

# One liner, but not readable
def duplicate_encode(word):
    return ''.join(['(' if word.lower().count(l.lower()) == 1 else ')' for l in word])
    
# Two liner, more readable, cleaner
def duplicate_encode(word):
    w = word.lower()
    return ''.join(['(' if w.count(l) == 1 else ')' for l in w])
    
    
Test.assert_equals(duplicate_encode("din"),"(((")
Test.assert_equals(duplicate_encode("recede"),"()()()")
Test.assert_equals(duplicate_encode("Success"),")())())")
Test.assert_equals(duplicate_encode("(( @"),"))((")
