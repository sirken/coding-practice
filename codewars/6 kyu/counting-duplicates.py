from Test import Test, Test as test

'''
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
'''

# Using total variable
def duplicate_count(text):
    data = list(text.lower())
    total = 0
    for letter in data:
        if data.count(letter) >= 2:
            total += 1
            while letter in data:
                data.remove(letter)
    return total

# Using length of list
def duplicate_count(text):
    output = []
    input = text.lower()
    for letter in input:
        if input.count(letter) > 1 and letter not in output:
            output.append(letter)
    return len(output)

# Create dictionary, which will not allow duplicates
# Return length of dictionary
def duplicate_count(text):
    x = text.lower()
    return len({y for y in x if x.count(y) > 1})

# Better, use set(), in which every value is unique
# Loop through the set so only going through each item once
# But get count from full item
def duplicate_count(text):
    return len({y for y in set(text.lower()) if text.lower().count(y) > 1})


test.assert_equals(duplicate_count("abcde"), 0)
test.assert_equals(duplicate_count("abcdea"), 1)
test.assert_equals(duplicate_count("indivisibility"), 1)
