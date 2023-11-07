"""
Exponential Search Algorithm

illustration,
li = [5, 9, 1, 6]

This algo depend on binarySearch algo.
Only index value multiple 2 till then findingKey <= li[index].

Time Complexity: O(log n)
"""

import time

from binarySearch import binarySearch

def exponentialSearch(lst, skey):
    if lst[0] == skey:
        return 0
    index = 1
    while index<len(lst) and lst[index] <= skey:
        index *= 2
    return BSA(lst[:index], skey)

*arr, = range(500)
print(arr)

while True:                                                                                                                                                                                                                                                 
    num = int(input("Enter number:"))
    if num == 0:
        break

    startTime = time.time()

    print(exponentialSearch(arr, num))
    
    endTime = time.time() - startTime
    
    print("/--------Exponential Search Algorithm------------/", endTime)
