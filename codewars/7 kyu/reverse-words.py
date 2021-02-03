from Test import Test, Test as test

'''
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''

def reverse_words(text):
    return ' '.join([word[::-1] for word in text.split(' ')])

test.assert_equals(reverse_words('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god')
test.assert_equals(reverse_words('apple'), 'elppa')
test.assert_equals(reverse_words('a b c d'), 'a b c d')
test.assert_equals(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')