from Test import Test

'''
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes:

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
'''

def high_and_low(numbers):
    n = numbers.split(' ')
    for num, i in enumerate(n):
        n[num] = int(i)
    return f'{max(n)} {min(n)}'

def high_and_low(numbers):
    n = [int(i) for i in numbers.split(' ')]
    return f'{max(n)} {min(n)}'


Test.assert_equals(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");
Test.assert_equals(high_and_low("1 2 3 4 5"), "5 1");
Test.assert_equals(high_and_low("1 9 3 4 -5"), "9 -5");
