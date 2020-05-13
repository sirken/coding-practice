from Test import Test, Test as test

'''
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples
maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"
'''

# return masked string
def maskify(cc):
    return '#' * (len(cc)-4) + cc[-4:]

cc = ''
r = maskify(cc)
test.describe("masking: {0}".format(cc))
test.it("{0}  matches  {1}".format(cc,r))
test.assert_equals(r, cc)

cc = '123'
r = maskify(cc)
test.describe("masking: {0}".format(cc))
test.it("{0}  matches  {1}".format(cc, r))
test.assert_equals(r, cc)

cc = 'SF$SDfgsd2eA'
r = maskify(cc)
test.describe("masking: {0}".format(cc))
test.it("{0}  matches  {1}".format('########d2eA', r))
test.assert_equals(r, '########d2eA')