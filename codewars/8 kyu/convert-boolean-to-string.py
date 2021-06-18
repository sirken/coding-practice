from Test import Test, Test as test

'''
Implement a function which convert the given boolean value into its string representation.

Note: Only valid inputs will be given.
'''

def boolean_to_string(b):
    return f'{b}'

test.assert_equals(boolean_to_string(True), "True")
test.assert_equals(boolean_to_string(False), "False")