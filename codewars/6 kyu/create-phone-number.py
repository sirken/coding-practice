from Test import Test, Test as test

'''
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
'''

# easy counter
def create_phone_number(n):
    output = ['(']
    for num, x in enumerate(n):
        if num == 3:
            output.append(') ')
        elif num == 6:
            output.append('-')
        output.append(str(x))
    return(''.join(output))

# skeleton and bones
def create_phone_number(n):
    skeleton = '(012) 345-6789'
    out = []
    for bone in skeleton:
        if bone.isdigit():
            out.append(str(n[int(bone)]))
        else:
            out.append(bone)
    return ''.join(out)

# compressed vertebrae
def create_phone_number(n):
    skeleton = '(012) 345-6789'
    return ''.join([str(n[int(bone)]) if bone.isdigit() else bone for bone in skeleton])

# Top - whaaaat?
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

Test.describe("Basic tests")
Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
Test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
Test.assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
Test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")