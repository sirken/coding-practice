from Test import Test, Test as test

'''
Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.

Can you help her?
'''

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"

Test.describe("Jenny's greeting function")
Test.it("should greet some people normally")
Test.assert_equals(greet("James"), "Hello, James!")
Test.assert_equals(greet("Jane"), "Hello, Jane!")
Test.assert_equals(greet("Jim"), "Hello, Jim!")

Test.it("should greet Johnny a little bit more special")
Test.assert_equals(greet("Johnny"), "Hello, my love!")