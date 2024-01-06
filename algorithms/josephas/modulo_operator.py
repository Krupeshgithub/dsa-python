"""
Josephus problem solved by python modulo operator
"""
from __future__ import annotations
import time


def modulo_operator(
    number: int,
    killer: int
) -> list(int):
    """
    We have to implement cirular list functionality with modulo operator.
    Time Complexity: O(n)
    Space Complexity: -
    """
    start_time = time.time()
    lst = list(range(1, number+1))
    steps = 1
    index = 0

    while len(list(filter(None, lst))) > 1:

        if lst[index] == 0:
            ...
        else:
            if steps == killer:
                steps = 1
                lst[index] = 0
            else:
                steps += 1
        index = (1 + index) % len(lst)
    print("Execution time: ", time.time() - start_time)
    return list(filter(None, lst))[0]

print("Output: ", modulo_operator(7000, 4))
