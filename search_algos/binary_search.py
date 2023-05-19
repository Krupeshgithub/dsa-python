"""
Binary Search Algorithm:

illustration,
li = [5, 9, 1, 6]

index = (low+high) // 2 ----> 2 # Find index 2 

if findingKey > index ----> high is 9 and low is 5

if findingKey < index ----> hight is 6 and low is 0


Time Complexity: O(log(n))
"""

import time

def binarySearch(arr, skey):
    first, last = 0, len(arr)-1

    while first<=last:
        mid = (first+last)//2

        if arr[mid] == skey:
            return mid

        if arr[mid] < skey:
            first = mid+1
        else:
            last = mid-1


*arr, = range(500)
print(arr)

while True:
    num = int(input("Enter number:"))
    if num == 0:
        break

    startTime = time.time()

    print(binarySearch(arr, num))
    
    endTime = time.time() - startTime
    
    print("/--------Binary Search Algorithm------------/", endTime)