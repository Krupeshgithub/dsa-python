"""
Impliment of Josephas Problem

>>> print(circular_list(7000000, 4))
Execution time: 38.2810s
Output: 532567
"""
from __future__ import annotations
import time


def circular_list(
    number: int,
    killer: int
) -> list(int):
    """
    Solve josephas problem with use list.
    Time Complexity: O(n^2)
    Space Complexity: -
    """ 
    start_time = time.time()
    steps = 1
    lst = list(range(1, number+1))

    while len(list(filter(None, lst))) > 1:

        for itr in range(0, number):
            if lst[itr] == 0:
                continue
            else:
                if steps != killer:
                    steps += 1
                    continue
                lst[itr] = 0
                steps = 1
    print("Execution time: ", time.time() - start_time)
    return list(filter(None, lst))[0]

print("Output: ", circular_list(7000, 4))
