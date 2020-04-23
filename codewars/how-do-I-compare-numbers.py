from Test import Test, Test as test

'''
What could be easier than comparing integer numbers? However, the given piece of code doesn't recognize some of the special numbers for a reason to be found. Your task is to find the bug and eliminate it.
'''

def what_is(x):
    if x is 42:
        return 'everything'
    elif x == 42 * 42:
        return 'everything squared'
    else:
        return 'nothing'


Test.describe('what_is')
Test.it('should work correctly')
tests = [
    (0, 'nothing'),
    (123, 'nothing'),
    (-1, 'nothing'),
    (42, 'everything'),
    (42 * 42, 'everything squared'),
]
for x, answer in tests:
    Test.assert_equals(what_is(x), answer)
