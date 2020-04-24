from Test import Test, Test as test

'''
Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.

Task
You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.

Examples
A size 3 diamond:

 *
***
 *
...which would appear as a string of " *\n***\n *\n"

A size 5 diamond:

  *
 ***
*****
 ***
  *
...that is: " *\n ***\n*****\n ***\n *\n"
'''

# While loop
def diamond(n):
    if n % 2 != 0 and n > 0:
        str = ''
        count = 1
        step = 2
        while count <= n and count > 0:
            str += ('*' * count).center(n, ' ').rstrip() + '\n'
            if count == n:
                step = -2
            count += step
        return str
    else:
        return None

def diamond(n):
    if n % 2 != 0 and n > 0:
        l = []
        count = 1
        step = 2
        while count <= n and count > 0:
            l.append(('*' * count).center(n, ' ').rstrip() + '\n')
            if count == n:
                step = -2
            count += step
        return ''.join(l)
    else:
        return None

# For loop
def diamond(n):
    if n % 2 != 0 and n > 0:
        str = ''
        for x in range(1, n, 2):
            str += ('*' * x).center(n, ' ').rstrip() + '\n'
        for x in range(n, 0, -2):
            str += ('*' * x).center(n, ' ').rstrip() + '\n'
        return str
    else:
        return None

# Add range lists together
def diamond(n):
    if n % 2 != 0 and n > 0:
        str = ''
        for x in list(range(1, n, 2)) + list(range(n, 0, -2)):
            str += ('*' * x).center(n, ' ').rstrip() + '\n'
        return str
    else:
        return None

def diamond(n):
    if n % 2 != 0 and n > 0:
        return ''.join([('*' * x).center(n, ' ').rstrip() + '\n' for x in list(range(1, n, 2)) + list(range(n, 0, -2))])
    else:
        return None

diamond(5)

expected =  " *\n"
expected += "***\n"
expected += " *\n"
test.assert_equals(diamond(1), "*\n")
test.assert_equals(diamond(2), None)
test.assert_equals(diamond(3), expected)
Test.assert_equals(diamond(5), "  *\n ***\n*****\n ***\n  *\n")
test.assert_equals(diamond(0), None)
test.assert_equals(diamond(-3), None)
