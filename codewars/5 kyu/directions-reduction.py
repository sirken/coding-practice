from Test import Test, Test as test

'''
Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, with dreadfull weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

How I crossed a mountain desert the smart way.
The directions given to the man are, for example, the following (depending on the language):

["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
You can immediatly see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay to the same place! So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:
["WEST"]
'''

d = dict(north='south', south='north', east='west', west='east')

def dirReduc(arr):
    reduced = False
    while not reduced:
        reduced = True
        for pos, dir in enumerate(arr[:-1]):
            if dir.lower() == d[arr[pos+1].lower()]:
                reduced = False
                del arr[pos:pos+2]
                break
    return arr


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
test.assert_equals(dirReduc(a), ['WEST'])
u=["NORTH", "WEST", "SOUTH", "EAST"]
test.assert_equals(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])
