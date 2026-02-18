"""
Complete the merge_sorted_lists function.

You are given two sorted lists of player levels (small integers). Each list is already in ascending order.

merge_sorted_lists should create and return one new list that:

contains all the values from both input lists
is also in ascending order
does not change the original lists
Use loops, indexes, and comparisons to merge the lists. Do not rely on just doing something like sorted(list1 + list2).

Rules
Both input lists are sorted in ascending order.
Levels are integers.
Either list may be empty.
You must return a new list.
Hints (high level)
Think about using two indexes:

Start both indexes at 0.
At each step, compare the current values from each list.
Append the smaller value to the result list.
Move forward in the list you just took the value from.
When you reach the end of one list, append all remaining values from the other list.
Examples
levels_a = [1, 4, 7]
levels_b = [2, 3, 8, 10]
print(merge_sorted_lists(levels_a, levels_b))
# [1, 2, 3, 4, 7, 8, 10]

levels_c = []
levels_d = [5, 6, 9]
print(merge_sorted_lists(levels_c, levels_d))
# [5, 6, 9]

levels_e = [2, 2, 5]
levels_f = [1, 2, 3]
print(merge_sorted_lists(levels_e, levels_f))
# [1, 2, 2, 2, 3, 5]
"""

def merge_sorted_lists(list1, list2):
    sorted_list = []
    new_list = []
    limit = 0
    shorter = 0

    if len(list1) == 0 and len(list2) == 0:
        return []
    elif len(list1) == 0:
        return list2
    elif len(list2) == 0:
        return list1

    if len(list1) <= len(list2):
        limit = len(list1)
        shorter = 1
    elif len(list1) > len(list2):
        limit = len(list2)
        shorter = 2
    

    for i in range(0, limit):
        if list1[i] <= list2[i]:
            sorted_list.append(list1[i])
            sorted_list.append(list2[i])
        else:
            sorted_list.append(list2[i])
            sorted_list.append(list1[i])
        if i + 1 >= limit:
            if shorter == 0:
                break
            elif shorter == 1:
                sorted_list += list2[i + 1:]
            else:
                sorted_list += list1[i + 1:]

    return sorted_list