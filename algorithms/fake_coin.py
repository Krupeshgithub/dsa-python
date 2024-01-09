#!/usr/bin/env python3
"""
A fake among a eight coins

Divide and conquer
Recursion
Time complexity: O(n)
"""
from __future__ import annotations
import time


def fake_coin(lst: list(int)) -> int:
    """
    Solved this with recursion method.
    method to solve question is `divide and conquer`.

    :param lst: weight of the coins. which include the fake coin weigt.

    >>> lst: list = [10, 10, 10, 8, 10, 10, 10, 10]
    >>> print(fake_coint(lst))
    8
    """
    global start_time
    start_time = time.time()
    # Base case
    if len(lst) == 1:
        return lst[0]

    # Induction
    divide_lst: int = len(lst) // 2
    if sum(lst[:divide_lst]) < sum(lst[divide_lst:]):
        # Left
        lst: list = lst[:divide_lst]
    else:
        # Right
        lst: list = lst[divide_lst:]

    # Hypothesis
    return fake_coin(lst)

lst: list = [10]*7 + [8]
print(fake_coin(lst=lst))
print("Execution time: ", time.time() - start_time)
