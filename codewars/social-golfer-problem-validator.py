from Test import Test, Test as test

'''
A group of N golfers wants to play in groups of G players for D days in such a way that no golfer plays more than once with any other golfer. For example, for N=20, G=4, D=5, the solution at Wolfram MathWorld is

 Mon:    ABCD    EFGH    IJKL    MNOP    QRST
 Tue:    AEIM    BJOQ    CHNT    DGLS    FKPR
 Wed:    AGKO    BIPT    CFMS    DHJR    ELNQ
 Thu:    AHLP    BKNS    CEOR    DFIQ    GJMT
 Fri:    AFJN    BLMR    CGPQ    DEKT    HIOS
Write a function that validates a proposed solution, a list of list of strings, as being a solution to the social golfer problem. Each character represents a golfer, and each string is a group of players. Rows represent days. The solution above would be encoded as:

 [
  ['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],
  ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
  ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],
  ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'],
  ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']
 ]
You need to make sure (1) that each golfer plays exactly once every day, (2) that the number and size of the groups is the same every day, and (3) that each player plays with every other player at most once.

So although each player must play every day, there can be particular pairs of players that never play together.

It is not necessary to consider the case where the number of golfers is zero; no tests will check for that. If you do wish to consider that case, note that you should accept as valid all possible solutions for zero golfers, who (vacuously) can indeed play in an unlimited number of groups of zero.
'''


def valid(a):

    # List of players
    player_list = ''.join(a[0])

    # Dictionary for holding player info
    player_stats = {}

    # Create dict structure
    for player in player_list:
        player_stats[player] = {'played': [], 'with': []}

    # Populate player stats
    for num, day in enumerate(a):
        # If the length of the day doesn't equal the first day
        if len(day) != len(a[0]):
            return False
        for group in day:
            # If the length of the group doesn't equal the first one
            if len(group) != len(a[0][0]):
                return False
            for player in group:
                # If this player didn't play day 1
                if player not in player_list:
                    return False
                # If player already played today
                if num in player_stats[player]['played']:
                    print(f'{other} already played today, return False')
                    return False
                else:
                    player_stats[player]['played'].append(num)
                for other in group:
                    if other != player:
                        if other in player_stats[player]['with']:
                            print(f'{other} already played with {player}, return False')
                            return False
                        else:
                            player_stats[player]['with'].append(other)

    # Check if each player golfed every day
    for player in player_stats:
        if len(player_stats[player]['played']) != len(a):
            print(f'{player} did NOT play all {len(a)} days')
            return False

    return True



test.describe("Simple Positive Tests")

# Satisfying the following case is optional; uncomment it if you like.
#test.it("accepts having no golfers at all")
#for s in ([], [[]], [[],[]], [[],[],[]]):
#    test.assert_equals(valid(s), True, "There are no conflicts with zero golfers")

test.it("can handle the two-player case")
s = [ ["AB"] ]
test.assert_equals(valid(s), True, "Two player, one day works")

test.it("can handle a four-player case")
s = [
    ["AB", "CD"],
    ["AD", "BC"],
    ["BD", "AC"]]
test.assert_equals(valid(s), True, "Four players, three days works")

test.it("can handle the case from Wolfram MathWorld")
s = [
    ['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],
    ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
    ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],
    ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'],
    ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']]
test.assert_equals(valid(s), True, "Wolfram MathWorld case works")

test.describe("Simple Negative Tests")

test.it("can detect days with different number of groups")
s = [
    ["AB", "CD", "EF", "GH"],
    ["AC", "BD", "EG", "FH"],
    ["AD", "CE"],
    ["AE", "BG", "CH", "FD"]]
test.assert_equals(valid(s), False, "Must reject day with fewer groups")

test.it("can detect two players appearing twice")
s = [
    ["ABC", "DEF"],
    ["ADE", "CBF"]]
test.assert_equals(valid(s), False, "Must reject B & C playing together twice")
