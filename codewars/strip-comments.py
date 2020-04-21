from Test import Test, Test as test

'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:
result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
'''

# Split by rows, then find earliest marker and extract string before it
def solution(string,markers):
    strings = string.split('\n')
    l = []
    for line in strings:
        pos = len(line)
        for m in markers:
            if m in line:
                if line.index(m) < pos:
                    pos = line.index(m)
        l.append(line[:pos].rstrip())
    return '\n'.join(l)

# Top solution, split list by \n, edit in place
def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)

# Top solution expanded
def solution(string,markers):
    # split by lines
    parts = string.split('\n')
    # Loop through markers
    for s in markers:
        # Loop through all lines, check for any markers
        # Split by marker, grab first item, and rstrip whitespace
        for num, v in enumerate(parts):
            parts[num] = v.split(s)[0].rstrip()
    return '\n'.join(parts)



Test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
Test.assert_equals(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
Test.assert_equals(solution('= - avocados oranges pears cherries\nlemons apples\n- watermelons strawberries', ['#', '?', '=', ',', '.', '-', '!']), '\nlemons apples\n')
