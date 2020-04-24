from Test import Test
'''
Complete the solution so that it reverses the string value passed into it.
'''

def solution(string):
    s = list(string)
    s.reverse()
    return ''.join(s)
    
def solution(string):
    s = ''
    for x in string:
        s = x + s
    return s

# Best practice
# Slice the entire list, step by -1
def solution(str):
  return str[::-1]


print(solution('this is a test'))
