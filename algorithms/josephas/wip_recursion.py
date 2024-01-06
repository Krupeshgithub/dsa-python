"""
Impliment of Josephas Problem
"""
from __future__ import annotations
import time


def recursion(
    number: int,
    killer: int
) -> list(int):
    """
    Solved josephas problem with use recursion.    
    """
    start_time = time.time()
    
    # Base case
    if number == 1:
        return 1

    # Hypothesis
    return  recursion()
