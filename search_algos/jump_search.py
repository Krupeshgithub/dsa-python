"""
Jump Search Algorithm

illustration,
li = [5, 9, 1, 6]

jump = int(math.sqrt(len(li))) = 2

Always jump 2 steps --> After find to search left element or right 

Note: Always low and high value different every 2 step jumps. So, in last we need to search on between low and high.

Time Complexity: O(sqrt(n))
"""

import math
import time


def jumpSearch(lst, skey):
    length = len(lst)
    left = right = 0
    jump = int(math.sqrt(length))
    while left < length:
        minValue = min(length-1, left+jump)
        if lst[minValue] >=  skey:
            break
        left += jump
    if lst[left] == skey:
        return left
    right = left - jump
    while right < length:
        if lst[right] == skey:
            return right
        right += 1

*arr, = range(500)
print(arr)

while True:
    num = int(input("Enter number:"))
    if num == 0:
        break

    startTime = time.time()

    print(jumpSearch(arr, num))
    
    endTime = time.time() - startTime
    
    print("/--------Jump Search Algorithm------------/", endTime)
