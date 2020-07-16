from Test import Test, Test as test

'''
However, just as she finished rating all exhibitions, she's off to an important fair, so she asks you to write a program that tells her the ratings of the items after one removed the lowest one. Fair enough.

Task
Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.

Examples
remove_smallest([1,2,3,4,5]) = [2,3,4,5]
remove_smallest([5,3,2,1,4]) = [5,3,2,4]
remove_smallest([2,2,1,2,1]) = [2,2,2,1]
'''

def remove_smallest(numbers):
    if len(numbers) == 0:
        return numbers
    else:
        l = []
        i = numbers.index(min(numbers))
        for pos, x in enumerate(numbers):
            if pos != i:
                l.append(x)
        return l

def remove_smallest(numbers):
    if len(numbers) > 0:
        l = []
        i = numbers.index(min(numbers))
        for pos, x in enumerate(numbers):
            if pos != i:
                l.append(x)
        return l
    return numbers

# cleaned up
def remove_smallest(numbers):
    if len(numbers) > 0:
        i = numbers.index(min(numbers))
        return [x for pos, x in enumerate(numbers) if pos != i]
    return numbers

# Top solution
def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a

Test.assert_equals(remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]")
Test.assert_equals(remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]")
Test.assert_equals(remove_smallest([1, 2, 3, 1, 1]), [2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]")
Test.assert_equals(remove_smallest([]), [], "Wrong result for []")