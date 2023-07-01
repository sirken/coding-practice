from Test import Test, Test as test

'''
Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?
'''

def round_to_next5(n):
    while n % 5 != 0:
        n += 1
    return n

inp = 0
out = round_to_next5(inp)
test.assert_equals(out, 0, "Input: {}".format(inp))

inp = 1
out = round_to_next5(inp)
test.assert_equals(out, 5, "Input: {}".format(inp))

inp = -1
out = round_to_next5(inp)
test.assert_equals(out, 0, "Input: {}".format(inp))

inp = 5
out = round_to_next5(inp)
test.assert_equals(out, 5, "Input: {}".format(inp))

inp = 7
out = round_to_next5(inp)
test.assert_equals(out, 10, "Input: {}".format(inp))

inp = 20
out = round_to_next5(inp)
test.assert_equals(out, 20, "Input: {}".format(inp))

inp = 39
out = round_to_next5(inp)
test.assert_equals(out, 40, "Input: {}".format(inp))