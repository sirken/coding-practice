from Test import Test, Test as test

'''
Positive integers have so many gorgeous features. Some of them could be expressed as a sum of two or more consecutive positive numbers.

Consider an Example :
10 , could be expressed as a sum of 1 + 2 + 3 + 4.
Task
Given Positive integer, N , Return true if it could be expressed as a sum of two or more consecutive positive numbers , OtherWise return false .

Notes
Guaranteed constraint : 2 ≤ N ≤ (2^32) -1 .

Input >> Output Examples:
* consecutiveDucks(9)  ==>  return (true)  //  9 , could be expressed as a sum of ( 2 + 3 + 4 ) or ( 4 + 5 ) . 
* consecutiveDucks(64)  ==>  return (false)
* consecutiveDucks(42)  ==>  return (true) //  42 , could be expressed as a sum of ( 9 + 10 + 11 + 12 )  .
'''

# Start at zero, work up
# Inefficient
def consecutive_ducks(n):
    for x in range(n):
        sum = 0
        for y in range(x, n):
            sum += y
            if sum == n:
                return True
            elif sum > n:
                break
    return False

# Reversed, start at middle and work down
# Still inefficient
def consecutive_ducks(n):
    for x in range(n//2+1, 0, -1):
        sum = 0
        for y in range(x, 0, -1):
            sum += y
            if sum == n:
                return True
            elif sum > n:
                break
    return False





test.assert_equals(consecutive_ducks(69), True)
test.assert_equals(consecutive_ducks(8), False)
test.assert_equals(consecutive_ducks(57), True)
test.assert_equals(consecutive_ducks(6), True)
test.assert_equals(consecutive_ducks(13), True)
test.assert_equals(consecutive_ducks(16), False)
test.assert_equals(consecutive_ducks(91), True)
test.assert_equals(consecutive_ducks(75), True)
test.assert_equals(consecutive_ducks(38), True)
test.assert_equals(consecutive_ducks(25), True)
test.assert_equals(consecutive_ducks(32), False)
test.assert_equals(consecutive_ducks(65), True)
test.assert_equals(consecutive_ducks(13), True)
test.assert_equals(consecutive_ducks(16), False)
test.assert_equals(consecutive_ducks(99), True)
'''
test.assert_equals(consecutive_ducks(522), True)
test.assert_equals(consecutive_ducks(974), True)
test.assert_equals(consecutive_ducks(755), True)
test.assert_equals(consecutive_ducks(512), False)
test.assert_equals(consecutive_ducks(739), True)
test.assert_equals(consecutive_ducks(1006), True)
test.assert_equals(consecutive_ducks(838), True)
test.assert_equals(consecutive_ducks(1092), True)
test.assert_equals(consecutive_ducks(727), True)
test.assert_equals(consecutive_ducks(648), True)
test.assert_equals(consecutive_ducks(1024), False)
test.assert_equals(consecutive_ducks(851), True)
test.assert_equals(consecutive_ducks(541), True)
test.assert_equals(consecutive_ducks(1011), True)
test.assert_equals(consecutive_ducks(822), True)

test.assert_equals(consecutive_ducks(382131), True)
test.assert_equals(consecutive_ducks(118070), True)
test.assert_equals(consecutive_ducks(17209), True)
test.assert_equals(consecutive_ducks(32768), False)
test.assert_equals(consecutive_ducks(161997), True)
test.assert_equals(consecutive_ducks(400779), True)
test.assert_equals(consecutive_ducks(198331), True)
test.assert_equals(consecutive_ducks(325482), True)
test.assert_equals(consecutive_ducks(88441), True)
test.assert_equals(consecutive_ducks(648), True)
test.assert_equals(consecutive_ducks(65536), False)
test.assert_equals(consecutive_ducks(323744), True)
test.assert_equals(consecutive_ducks(183540), True)
test.assert_equals(consecutive_ducks(65271), True)
test.assert_equals(consecutive_ducks(5263987), True)
'''