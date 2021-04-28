from Test import Test, Test as test

'''
Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".
'''

def greet(name):
    return f'Hello, {name} how are you doing today?'




test.assert_equals(greet('Ryan'), "Hello, Ryan how are you doing today?")
test.assert_equals(greet('Shingles'), "Hello, Shingles how are you doing today?")
