from Test import Test, Test as test

'''
If you can't sleep, just count sheep!!

Task:
Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.
'''


def count_sheep(n):
    return ''.join([f'{i+1} sheep...' for i in range(n)])

test.assert_equals(count_sheep(1), "1 sheep...");
test.assert_equals(count_sheep(2), "1 sheep...2 sheep...")
test.assert_equals(count_sheep(3), "1 sheep...2 sheep...3 sheep...")