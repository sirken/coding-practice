from Test import Test, Test as test

'''
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
'''

def bool_to_word(boolean):
    if boolean: return 'Yes'
    return 'No'

# Top
def bool_to_word(bool):
    return "Yes" if bool else "No"

test.assert_equals(bool_to_word(True), 'Yes')
test.assert_equals(bool_to_word(False), 'No')
