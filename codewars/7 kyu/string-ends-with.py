from Test import Test, Test as test

'''
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
'''

def solution(string, ending):
    return True if string[-len(ending):] == ending or len(ending) == 0 else False

# Top solution
def solution(string, ending):
    return string.endswith(ending)

test.assert_equals(solution('abcde', 'cde'), True)
test.assert_equals(solution('abcde', 'abc'), False)
test.assert_equals(solution('abcde', ''), True)