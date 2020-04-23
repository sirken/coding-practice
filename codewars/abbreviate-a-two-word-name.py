from Test import Test, Test as test

'''
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F
'''

# Basic
def abbrevName(name):
    n = name.upper().split(' ')
    return f'{n[0][0]}.{n[1][0]}'

# Wordy
def abbrevName(name):
    return '.'.join(list(map(lambda x: x[0], name.upper().split(' '))))

# Top solution
def abbrevName(name):
    return '.'.join([x[0] for x in name.upper().split()])



Test.assert_equals(abbrevName("Sam Harris"), "S.H")
Test.assert_equals(abbrevName("Patrick Feenan"), "P.F")
Test.assert_equals(abbrevName("Evan Cole"), "E.C")
Test.assert_equals(abbrevName("P Favuzzi"), "P.F")
Test.assert_equals(abbrevName("David Mendieta"), "D.M")