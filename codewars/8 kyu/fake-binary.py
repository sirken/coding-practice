from Test import Test, Test as test

'''
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
'''

def fake_bin(x):
    output = ''
    for i in x:
        if int(i) < 5:
            output += '0'
        else:
            output += '1'
    return output

# Clever one
def fake_bin(s):
    return s.translate(string.maketrans('0123456789', '0000011111'))

# Nice, but not as readable
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)

test.describe("Example Tests")
tests = [
    # [expected, input]
    ["01011110001100111", "45385593107843568"],
    ["101000111101101", "509321967506747"],
    ["011011110000101010000011011", "366058562030849490134388085"],
    ["01111100", "15889923"],
    ["100111001111", "800857237867"],
]

for exp, inp in tests:
    test.assert_equals(fake_bin(inp), exp)