from Test import Test, Test as test

'''
Create a function that given a sequence of strings, groups the elements that can be obtained by rotating others, ignoring upper or lower cases.

In the event that an element appears more than once in the input sequence, only one of them will be taken into account for the result, discarding the rest.

Input
Sequence of strings. Valid characters for those strings are uppercase and lowercase characters from the alphabet and whitespaces.

Output
Sequence of elements. Each element is the group of inputs that can be obtained by rotating the strings.

Sort the elements of each group alphabetically.

Sort the groups descendingly by size and in the case of a tie, by the first element of the group alphabetically.

Examples
['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris', 'Okyot'] --> [['Kyoto', 'Okyot', 'Tokyo'], ['Donlon', 'London'], ['Paris'], ['Rome']]

['Rome', 'Rome', 'Rome', 'Donlon', 'London'] --> [['Donlon', 'London'], ['Rome']]

[] --> []
'''

def check_rotate(word1, word2):
    for pos, letter in enumerate(word1):
        if f'{word1[pos:]}{word1[:pos]}'.lower() == word2.lower():
            return True
    return False


def group_cities(seq):
    out = []
    for city in seq:
        l = sorted({c for c in seq if check_rotate(city, c)})
        if l not in out:
            out.append(l)
    out.sort()
    out.sort(key=len, reverse=True)
    return out





test.assert_equals(group_cities(['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris', 'Okyot']),
                   [['Kyoto', 'Okyot', 'Tokyo'], ['Donlon', 'London'], ['Paris'], ['Rome']])

test.assert_equals(group_cities(['Tokyo', 'London', 'Rome', 'Donlon']),
                   [['Donlon', 'London'], ['Rome'], ['Tokyo']])

test.assert_equals(group_cities(['Aab', 'Baa', 'Abbc', 'Cbba', 'Ba']),
                   [['Aab', 'Baa'], ['Abbc'], ['Ba'], ['Cbba']])

test.assert_equals(group_cities(['Rome', 'Rome', 'Rome', 'Donlon', 'London']), [['Donlon', 'London'], ['Rome']])
test.assert_equals(group_cities(['Ab', 'Aa']), [['Aa'], ['Ab']])
test.assert_equals(group_cities([]), [])
