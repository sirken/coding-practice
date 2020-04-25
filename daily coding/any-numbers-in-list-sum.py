'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''


def check_2_numbers(anum, alist):
    for x in alist:
        #print(f'Start {x}')
        for y in alist[alist.index(x)+1:]:
            #print(f'- check {y}')
            if x + y == anum:
                return True
    return False


print(check_2_numbers(17, [10, 15, 3, 7]))
print(check_2_numbers(19, [10, 15, 3, 7]))