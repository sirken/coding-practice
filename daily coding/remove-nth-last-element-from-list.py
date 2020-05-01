from Test import Test

'''
Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
'''

def del_from_list(arr, k):
    del(arr[-k])
    return arr

def del_from_list(arr, k):
    return [i for i in arr if i != arr[-k]]

Test.assert_equals(del_from_list([10, 15, 3, 7], 1), [10, 15, 3])
Test.assert_equals(del_from_list([10, 15, 3, 7], 2), [10, 15, 7])
Test.assert_equals(del_from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 5), [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13])
