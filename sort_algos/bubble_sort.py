"""
# Bubble_sort 

Simple sorting algorithm. 
Repeatedly swapping each elements.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""
import time

start_time = time.time()

def bubbleSort(array: list[int]) -> list[int]:
        swapped = True
        for i in range(len(array)):
            


array = [38, 41, 25, 42, 35, 19, 45, 12, 33, 21, 0, 47, 18, 15, 26, 29, 30,
        32, 27, 43, 22, 34, 31, 44, 46, 40, 49, 9, 39, 14, 3, 8, 17, 48, 23, 
        6, 13, 36, 28, 1, 5, 10, 37, 16, 2, 24, 4, 7, 11, 20]


itr_time = time.time() - start_time
print("sorted array:", bubbleSort(array))
print("time taken:", itr_time)