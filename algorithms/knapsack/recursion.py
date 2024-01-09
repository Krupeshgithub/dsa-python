#!/usr/bin/env python3
"""
Solve knapsack problem with recursion approach.
"""
from __future__ import annotations
import time


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
    if (length == 0 or capacity == 0):
        return 0
    
    # Hypothesis
    if (capacity >= weight[length - 1]):
        return max(
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
    else:
        return knapsack(
                weight=weight,
                value=value,
                length=length-1,
                capacity=capacity
            )

print(knapsack(
    weight=[2, 3, 4, 7, 14, 15, 10, 12, 13, 52, 24, 31, 95, 45],
    value=[10, 20, 30, 40, 50, 10, 20, 30, 10, 50, 70, 60, 40, 20],
    length=14,
    capacity=140
))
print("Execution time: ", time.time() - start_time)
