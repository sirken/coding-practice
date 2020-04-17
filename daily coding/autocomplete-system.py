'''
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''

def get_prefix(prefix, alist):
    return [word for word in alist if word[0:2] == prefix]


print(get_prefix('de', ['dog', 'deer', 'deal', 'dime', 'dodo','dead']))
print(get_prefix('ba', ['bag', 'beds', 'barn', 'bunny', 'bake','bored']))
