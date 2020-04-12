from Test import Test

'''
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
'''

def filter_list(l):
    return [x for x in l if type(x) is int]

# Use isinstance because it supports inheritance
# https://stackoverflow.com/questions/1549801/what-are-the-differences-between-type-and-isinstance
# Also, better to remove strings instead of only including integers
def filter_list(l):
    return [x for x in l if not isinstance(x, str)]


Test.assert_equals(filter_list([1,2,'a','b']),[1,2])
Test.assert_equals(filter_list([1,'a','b',0,15]),[1,0,15])
Test.assert_equals(filter_list([1,2,'aasf','1','123',123]),[1,2,123])
