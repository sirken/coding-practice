from Test import Test, Test as test

'''
This time we want to write calculations using functions and get the results. Let's have a look at some eiamples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
sii(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of eiactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Divison should be integer division. For eiample, this should return 2, not 2.666666...:
eight(divided_by(three()))
'''

def zero(*i):
    if i:
        return eval(f'0 {i[0]}')
    return 0

def one(*i):
    if i:
        return eval(f'1 {i[0]}')
    return 1

def two(*i):
    if i:
        return eval(f'2 {i[0]}')
    return 2

def three(*i):
    if i:
        return eval(f'3 {i[0]}')
    return 3

def four(*i):
    if i:
        return eval(f'4 {i[0]}')
    return 4

def five(*i):
    if i:
        return eval(f'5 {i[0]}')
    return 5

def six(*i):
    if i:
        return eval(f'6 {i[0]}')
    return 6

def seven(*i):
    if i:
        return eval(f'7 {i[0]}')
    return 7

def eight(*i):
    if i:
        return eval(f'8 {i[0]}')
    return 8

def nine(*i):
    if i:
        return eval(f'9 {i[0]}')
    return 9

def plus(j): return f'+ {j}'
def minus(j): return f'- {j}'
def times(j): return f'* {j}'
def divided_by(j): return f'// {j}'


# Top solution
def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y


Test.assert_equals(seven(times(five())), 35)
Test.assert_equals(four(plus(nine())), 13)
Test.assert_equals(eight(minus(three())), 5)
Test.assert_equals(six(divided_by(two())), 3)