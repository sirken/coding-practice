from Test import Test

'''
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
'''

def accum(s):
    l = []
    for n, i in enumerate(s, start=1):
        l.append((i*n).title())
    return '-'.join(l)

def accum(s):
    return '-'.join([(i*n).title() for n, i in enumerate(s, start=1)])

# Top solution, nice thinking
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


Test.describe("accum")
Test.it("Basic tests")
Test.assert_equals(accum("ZpglnRxqenU"),
                   "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
Test.assert_equals(accum("NyffsGeyylB"),
                   "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")
Test.assert_equals(accum("MjtkuBovqrU"),
                   "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu")
Test.assert_equals(accum("EvidjUnokmM"),
                   "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm")
Test.assert_equals(accum("HbideVbxncC"),
                   "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc")