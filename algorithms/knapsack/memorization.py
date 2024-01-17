#!/usr/bin/env python3
"""
Let's solve this question with Dynamic Progamming.

We impliment memorization approach for solving this same problem.
For this method, we have to store every repeated values into the matrix.
"""
from __future__ import annotations
import time
import numpy as np


def knapsack(
    weight: list[int] = [],
    value: list[int] = [],
    length: int = 0,
    capacity: int = 0
) -> int:
    """
    :param weight: weights of the every items which will put inside the knapsack.
    :param value: values of the every items which present the price.
    :param length: length of all items.
    :param capacity: maximum capacity to put items inside the knapsack.
    """
    global start_time
    start_time = time.time()
    # Base case
    if (length == 0 or weight == 0):
        return 0

    # Induction
    # If the values inside the matrix then just simple return the value
    if T[length][capacity] != 1:
        return T[length][capacity]

    # Hypothesis
    if (capacity >= weight[length - 1]):
        resp = max(
            value[length - 1]
            + knapsack(
                weight=weight,
                value=value,
                length=length-1,
                capacity=capacity-weight[length-1]
            ),
            knapsack(
                weight=weight,
                value=value,
                length=length-1,
                capacity=capacity
            )
        )
        return resp
    else:
        # Repeated part
        T[length][capacity] = knapsack(
                weight=weight,
                value=value,
                length=length-1,
                capacity=capacity
            )
        return T[length][capacity]


T = np.ones([14+1, 140+1], int)
print(knapsack(
    weight=[2, 3, 4, 7, 14, 15, 10, 12, 13, 52, 24, 31, 95, 45],
    value=[10, 20, 30, 40, 50, 10, 20, 30, 10, 50, 70, 60, 40, 20],
    length=14,
    capacity=140
))
print("Execution time: ", time.time() - start_time)
