from Test import Test, Test as test

'''
Rock Paper Scissors
Let's play! You have to return which player won! In case of a draw return Draw!.

Examples:

rps('scissors','paper') // Player 1 won!
rps('scissors','rock') // Player 2 won!
rps('paper','paper') // Draw!
'''

def rps(p1, p2):
    p = ['paper','scissors','rock']
    if p1 == p2:
        return "Draw!"
    elif p[p.index(p1)-1] == p2:
        return "Player 1 won!"
    return "Player 2 won!"

# Top solution - more readable
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    elif beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"




Test.describe('rock paper scissors')
Test.it('player 1 win')
Test.assert_equals(rps('rock', 'scissors'), "Player 1 won!")
Test.assert_equals(rps('scissors', 'paper'), "Player 1 won!")
Test.assert_equals(rps('paper', 'rock'), "Player 1 won!")

Test.it('player 2 win')
Test.assert_equals(rps('scissors', 'rock'), "Player 2 won!")
Test.assert_equals(rps('paper', 'scissors'), "Player 2 won!")
Test.assert_equals(rps('rock', 'paper'), "Player 2 won!")

Test.it('draw')
Test.assert_equals(rps('rock', 'rock'), 'Draw!')
Test.assert_equals(rps('scissors', 'scissors'), 'Draw!')
Test.assert_equals(rps('paper', 'paper'), 'Draw!')