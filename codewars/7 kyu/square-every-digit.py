from Test import Test, Test as test

'''
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
'''

def square_digits(num):
    return int(''.join([str(int(x) ** 2) for x in str(num)]))
    
    
    
test.assert_equals(square_digits(9119), 811181)
