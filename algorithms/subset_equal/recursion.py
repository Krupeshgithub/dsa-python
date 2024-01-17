"""
This problem are seminal with suset_sum,

Discusion: For input we have given array,
We need to divide this array into equal parts which subsets are equal sum.

lst = [1, 5, 11, 5]
subset_1 = [1, 5, 5]
subset_2 = [11]
"""
from __future__ import annotations
import time


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
    if (len(lst) % 2 != 0) or (length == 0 or number == 0):
        return 0

    # Hypothesis
    if (number >= lst[length - 1]):
        return max(
            lst[length-1]
            + subset_sum(lst, number-lst[length-1], length-1),
            subset_sum(lst, number, length-1)
        )
    else:
        return subset_sum(lst, number, length-1)


lst = [1, 5, 11, 5]
resp = subset_sum(
    lst=lst,
    number=sum(lst)//2,
    length=len(lst)
)
print(resp == sum(lst)//2)
print("Execution time: ", time.time() - start_time)
