from Test import Test, Test as test

'''
Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
'''

def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

test.assert_equals(even_or_odd(2), "Even")
test.assert_equals(even_or_odd(0), "Even")
test.assert_equals(even_or_odd(7), "Odd")
test.assert_equals(even_or_odd(1), "Odd")
test.assert_equals(even_or_odd(-1), "Odd")
