from Test import Test, Test as test

'''
Your function takes two arguments:

current father's age (years)
current age of his son (years)
Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old). The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.
'''

def twice_as_old(dad, son):
    yrs = 0
    while True:
        if dad + yrs == (son + yrs) * 2 or dad - yrs == (son - yrs) * 2:
            break
        yrs += 1
    return yrs

# abs to the rescue
def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2*son_years_old)



test.assert_equals(twice_as_old(36, 7), 22)
test.assert_equals(twice_as_old(55, 30), 5)
test.assert_equals(twice_as_old(42, 21), 0)
test.assert_equals(twice_as_old(22, 1), 20)
test.assert_equals(twice_as_old(29, 0), 29)
