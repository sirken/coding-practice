from Test import Test, Test as test

'''
Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".
'''

def problem(a):
    try:
        return a * 50 + 6
    except:
        return 'Error'

test.assert_equals(problem("hello"), "Error")
test.assert_equals(problem(1), 56)