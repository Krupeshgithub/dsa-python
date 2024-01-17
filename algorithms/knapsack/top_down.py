"""Solved knapsack problem with top down approach."""
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

    # Hypothesis
    # We need to nested interation for solve knapsack problem.
    for itr in range(1, length+1):
        for jtr in range(1, capacity+1):

            # Induction
            if (jtr >= weight[itr - 1]):
                T[itr][jtr] =  max(
                    value[itr - 1]
                    + T[itr-1][jtr-weight[itr-1]],
                    + T[itr-1][jtr]
                )
            else:
                T[itr][jtr] = T[itr-1][jtr]

    return T[length][capacity]


T = np.ones([14+1, 140+1], int)
print(knapsack(
    weight=[2, 3, 4, 7, 14, 15, 10, 12, 13, 52, 24, 31, 95, 45],
    value=[10, 20, 30, 40, 50, 10, 20, 30, 10, 50, 70, 60, 40, 20],
    length=14,
    capacity=140
))
print("Execution time: ", time.time() - start_time)
