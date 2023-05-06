"""
# Selection_sort

We continuosuly remove the smallest element from the
unsorted segment of the list and append it to the sorted segment.

illustration,
li = [5, 9, 1, 6]

first = [5, 9, 1, 6] is 5 > 9 ? No
second = [1, 9, 5, 6] is 5 > 1 ? Yes
thired = [1, 9, 5, 6] is 1 > 6 ? No
forth = [1, 5, 9, 6] is 9 > 5 ? Yes
fifth = [1, 5, 9, 6] is 5 > 6 ? No
six = [1, 5, 6, 9] is 9 > 6 ? Yes

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

import time

starting = time.time()

def selectSort(array):
    for itr in range(len(array)-1):
        for jtr in range(itr+1, len(array)):
            if array[itr] > array[jtr]:
                array[itr], array[jtr] = array[jtr], array[itr]
            else:
                continue
    return array            
        

array = [38, 41, 25, 42, 35, 19, 45, 12, 33, 21, 0, 47, 18, 15, 26, 29, 30,
         32, 27, 43, 22, 34, 31, 44, 46, 40, 49, 9, 39, 14, 3, 8, 17, 48, 23,
         6, 13, 36, 28, 1, 5, 10, 37, 16, 2, 24, 4, 7, 11, 20]


itr_time = time.time() - starting
print("sorted array:", selectSort(array))
print("time taken:", itr_time)