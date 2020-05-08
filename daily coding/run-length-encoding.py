from Test import Test
'''
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
'''

# Either look-ahead, or look-behind
# Track number of repeated characters

def run_len_encode(string):
    run = 0
    prev_char = ''
    out = ''
    for step, i in enumerate(string, start=1):
        if prev_char == '':
            run += 1
        else:
            if i == prev_char:
                run += 1
                if step == len(string):
                    out = f'{out}{run}{prev_char}'
            else:
                out = f'{out}{run}{prev_char}'
                run = 1
                if step == len(string):
                    out = f'{out}{run}{i}'
        prev_char = i
    return out



Test.assert_equals(run_len_encode('AAAABBBCCDAA'), '4A3B2C1D2A')
Test.assert_equals(run_len_encode('ABCDCCCCCDDA'), '1A1B1C1D5C2D1A')