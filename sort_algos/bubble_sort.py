"""
# Bubble_sort

Simple sorting algorithm.
Repeatedly swapping each elements.

illustration,
li = [5, 9, 1, 6]

first = [5, 9, 1, 6] is 5 > 9 ? No
second = [5, 1, 9, 6] is 9 > 1 ? Yes
thired =  [5, 1, 6, 9] is 9 > 6 ? Yes
forth = [1, 5, 6, 9] is 5 > 1 ? Yes
fifth = [1, 5, 6, 9] is 5 > 6 ? No
six = [1, 5, 6, 9] is 6 > 9 ? No
seven = [1, 5, 6, 9] is 1 > 5 ? No
eight = [1, 5, 6, 9] is 5 > 6 ? No
nine = [1, 5, 6, 9] is 6 > 9 ? No


Time Complexity: O(n^2)
Space Complexity: O(1)
"""

import time

starting = time.time()

def bubbleSort(array):
    swapped = True
    while swapped:
        swapped = False
        for itr in range(len(array)-1):
            if array[itr] > array[itr+1]:
                array[itr], array[itr+1] = array[itr+1], array[itr]
                swapped = True
    return array

array = [38, 41, 25, 42, 35, 19, 45, 12, 33, 21, 0, 47, 18, 15, 26, 29, 30,
         32, 27, 43, 22, 34, 31, 44, 46, 40, 49, 9, 39, 14, 3, 8, 17, 48, 23,
         6, 13, 36, 28, 1, 5, 10, 37, 16, 2, 24, 4, 7, 11, 20]


itr_time = time.time() - starting
print("sorted array:", bubbleSort(array))
print("time taken:", itr_time)
