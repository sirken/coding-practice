from Test import Test

'''
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
'''
# Failed @ codewars
def unique_in_order(iterable):
    l = [iterable[0]]
    for i in iterable:
        if i != l[-1]:
            l.append(i)
    return l

# Failed @ codewars
def unique_in_order(iterable):
    l = [iterable[0]]
    for num, i in enumerate(iterable[1:]):
        if i != iterable[num]:
            l.append(i)
    return l

# Accepted
def unique_in_order(iterable):
    l = []
    for i in iterable:
        if len(l) == 0:
            l.append(i)
        elif i != l[-1]:
            l.append(i)
    return l

# Highest voted
def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable:
        if char != prev:
            result.append(char)
            prev = char
    return result

Test.assert_equals(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])
Test.assert_equals(unique_in_order('ABBCcAD'), ['A', 'B', 'C', 'c', 'A', 'D'])
Test.assert_equals(unique_in_order([1,2,2,3,3]), [1,2,3])
Test.assert_equals(unique_in_order(['A']), ['A'])
