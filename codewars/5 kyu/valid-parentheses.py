from Test import Test, Test as test

'''
Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
'''

def valid_parentheses(string):
    pos = 0
    for i in string:
        if i == '(':
            pos += 1
        elif i == ')':
            pos -= 1
        if pos < 0:
            return False
    if pos == 0:
        return True
    return False

# Top solution, more readable
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False


Test.assert_equals(valid_parentheses("  ("), False)
Test.assert_equals(valid_parentheses(")test"), False)
Test.assert_equals(valid_parentheses(""), True)
Test.assert_equals(valid_parentheses("hi())("), False)
Test.assert_equals(valid_parentheses("hi(hi)()"), True)