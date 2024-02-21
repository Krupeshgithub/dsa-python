"""
Subset equal problem

- For this problem you will provide list of items and one integer number.
you have to find that the combine items equal sum is integer item or not.

lst = [1, 5, 11, 5]
number = 11
length = len(lst)

>>> recursion(lst, number, length)
Any int value
"""
from __future__ import annotations
import time
import numpy as np


def subset_sum(
    lst: list[int],
    number: int,
    length: int
) -> int:
    """
    :param lst: weights of the every items which will put inside the knapsack.
    :param length: length of all items.
    :param number: maximum capacity to put items inside the knapsack.
    """
    global start_time
    start_time = time.time()
    # Base case
    if ((len(lst) % 2 != 0)) or (number == 0 or length == 0):
        return 0
    
    if T[length][number] != 1:
        return T[length][number]

    # Hypothesis
    if (number >= lst[length - 1]):
        resp = max(
            lst[length-1]
            + subset_sum(lst, number-lst[length-1], length-1),
            subset_sum(lst, number, length-1)
        )
        return resp
    else:
        T[length][number] = subset_sum(lst, number, length-1)
        return T[length][number]


lst = [1, 2, 3, 5]
T = np.ones([len(lst)+1, sum(lst)+1], int)
resp = subset_sum(
    lst=lst,
    number=sum(lst)//2,
    length=len(lst)
)
print(resp == sum(lst)//2)
print("Execution time: ", time.time() - start_time)
