from Test import Test, Test as test

'''
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
'''

def iq_test(n):

    even = False
    odd = False

    if len([i for i in n.split() if int(i) % 2]) == 1:
        even = True
    else:
        odd = True

    for pos, i in enumerate(n.split(), start=1):
        if int(i) % 2 and even == True:
            return pos
        elif not int(i) % 2 and odd == True:
            return pos



Test.assert_equals(iq_test("2 4 7 8 10"), 3)
Test.assert_equals(iq_test("1 2 2"), 1)