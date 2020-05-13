from Test import Test

'''
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8
'''

def row_sum_odd_numbers(n):
    lst = [None]
    odd = 1
    count = 1
    for i in range(1, n+1):
        sub_lst = []
        for j in range(1, count+1):
            sub_lst.append(odd)
            odd += 2
        lst.append(sub_lst)
        count += 1
    return sum(lst[n])

# Top one, mind blown
def row_sum_odd_numbers(n):
    return n ** 3

Test.assert_equals(row_sum_odd_numbers(1), 1)
Test.assert_equals(row_sum_odd_numbers(2), 8)
'''
Test.assert_equals(row_sum_odd_numbers(13), 2197)
Test.assert_equals(row_sum_odd_numbers(19), 6859)
Test.assert_equals(row_sum_odd_numbers(41), 68921)
'''