from Test import Test, Test as test

'''
No Story

No Description

Only by Thinking and Testing

Look at the result of testcase, guess the code!
'''

def test_it(a, b):
    return sum([int(x) for x in str(a)]) * sum([int(y) for y in str(b)])


# Hmm.. 0 * 1 = 0
test.assert_equals(test_it(0, 1), 0)

# Yes, 1 * 2 = 2
test.assert_equals(test_it(1, 2), 2)

# I know, 5 * 6 = 30
test.assert_equals(test_it(5, 6), 30)

# What? 10 * 10 = 1 ?
test.assert_equals(test_it(10, 10), 1)

# Damn.. 200 * 200 = 4, 0 was omitted ?
test.assert_equals(test_it(200, 200), 4)

# Discover the mysteries of it ;-)
test.assert_equals(test_it(12, 34), 21)

# You can solve it
test.assert_equals(test_it(123, 45), 54)
