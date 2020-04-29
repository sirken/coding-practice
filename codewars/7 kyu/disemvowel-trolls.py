from Test import Test, Test as test

'''
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
'''

def disemvowel(string):
    return ''.join(x for x in string if x.lower() not in ('a','e','i','o','u'))

def disemvowel(string):
    return ''.join(x for x in string if x.lower() not in ('aeiou'))

def disemvowel(string):
    return string.translate(string.maketrans('','','aeiouAEIOU'))

test.assert_equals(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")