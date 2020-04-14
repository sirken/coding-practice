from Test import Test, Test as test

'''
Build Tower
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

for example, a tower of 3 floors looks like below

[
  '  *  ',
  ' *** ',
  '*****'
]
and a tower of 6 floors looks like below

[
  '     *     ',
  '    ***    ',
  '   *****   ',
  '  *******  ',
  ' ********* ',
  '***********'
]
'''

# Initial
def tower_builder(n_floors):
    total_len = n_floors * 2 - 1
    l = []
    for x in range(1, n_floors+1):
        a = '*' * (x * 2 - 1)
        a = a.center(total_len, ' ')
        l.append(a)
    return l

# Condensed
def tower_builder(n_floors):
    return [('*' * (x*2-1)).center(n_floors*2-1) for x in range(1, n_floors+1)]



test.describe("Tests")
test.it("Basic Tests")
test.assert_equals(tower_builder(1), ['*', ])
test.assert_equals(tower_builder(2), [' * ', '***'])
test.assert_equals(tower_builder(3), ['  *  ', ' *** ', '*****'])
