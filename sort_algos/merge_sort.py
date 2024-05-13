"""
This Algorithm works Like Dived And Conquer.
Which is work with recursion method.

One, array cut it into smallest part; and merge into the smallest part
"""

def merge_sorted_array(left, right):
    i = len(left)-1; j = len(right)-1
    tmp = []
    while i >= 0 and j >= 0:
        if left[i] >= right[j]:
            tmp.append(left[i]); i -= 1
        else:
            tmp.append(right[j]); j -= 1
    while i >= 0:
        tmp.append(left[i])
        i -= 1
    while j >= 0:
        tmp.append(right[j])
        j -= 1
    return tmp[::-1]


def merge_sort(array):
    if len(array) <= 1: return array

    mid = len(array) // 2

    sleft = merge_sort(array=array[:mid])
    sright = merge_sort(array=array[mid:])

    return merge_sorted_array(sleft, sright)

print(merge_sort([5,6,4,7,9,10,32,45]))