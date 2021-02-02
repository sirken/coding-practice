from Test import Test, Test as test

'''
Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.
'''

def clean_string(s):
    out = []
    for i in s:
        if i != '#':
            out.append(i)
        else:
            out = out[:-1]
    return ''.join(out)

Test.assert_equals(clean_string('abc#d##c'), "ac")
Test.assert_equals(clean_string('abc####d##c#'), "" )
Test.assert_equals(clean_string("#######"), "" )
Test.assert_equals(clean_string(""), "" )