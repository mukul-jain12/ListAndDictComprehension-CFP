"""
    @File :   filter_reduce_map.py
    @Author : mukul
    @Date :   23-12-2021
"""
from functools import reduce

# Filter Number divisible by 5
result = filter(lambda item: item % 5 == 0, (15, 30, 56, 64, 85, 90, 124, 149))
result = list(result)
print(result)

# Filter item from nested list
nested_list = [
    ['item1', 13940],
    ['item2', 32987],
    ['item3', 13260],
    ['item4', 26702]
]
filtered = filter(lambda item: item[1] > 30000, nested_list)
print(list(filtered))

# Sum of two lists using map
list1 = [12, 52, 21, 32, 54]
list2 = [49, 45, 85, 54, 98]

new_list = map(lambda item1, item2: item1 + item2, list1, list2)
print(list(new_list))

list3 = [12, 52, 21, 32, 54]

# using reduce to sum of list elements
result = reduce(lambda sum, item: sum + item, list3)
print("The sum of the list elements is : ", result)

# using reduce to find out maximum element from list
result = reduce(lambda num, item: num if num > item else item, list3)
print("The maximum element of the list is : ", result)
