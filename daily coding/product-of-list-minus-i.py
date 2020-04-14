'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

# List manipulation
def get_product(the_list):

    final_list = []

    for num, i in enumerate(the_list):
        # Create temporary copy of the_list
        tmp_list = the_list[:]
        # Delete the current item
        del tmp_list[num]
        # Return product of the rest of the list
        prod = 1
        for j in tmp_list:
            prod *= j
        # Store product in final_list
        final_list.append(prod)

    return final_list

# Using division
def get_product(the_list):

    final_list = []

    for i in the_list:
        prod = 1
        for j in the_list:
            prod *= j
        prod /= i
        final_list.append(int(prod))
    return final_list

# No division, replace list item with 1
def get_product(the_list):

    final_list = []

    for num, i in enumerate(the_list):
        tmp_list = the_list[:]
        tmp_list[num] = 1

        prod = 1
        for j in tmp_list:
            prod *= j

        final_list.append(prod)
    return final_list



print(get_product([1,2,3,4,5]))
print(get_product([3,2,1]))
