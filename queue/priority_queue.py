#!/usr/bin/env python3
"""Implimenting priority queue using list"""
from __future__ import annotations

from typing import Any


class OverFlowError(Exception):
    pass


class UnderFlowError(Exception):
    pass


class FixedPriorityQueue:
    """
    Tasks can be added to a Priority Queue at any time and in any order but when tasks
    are removed then the Task with higher priority removed in FIFO queue.
    In the code will set three levels of priority.
    >>> fpq = FixPriorityQueue()
    >>> fpq.enqueue(0, 10)
    >>> fpq.enqueue(1, 70)
    >>> fpq.enqueue(0, 100)
    >>> fpq.enqueue(2, 1)
    >>> fpq.enqueue(2, 5)
    >>> fpq.enqueue(1, 7)
    >>> fpq.enqueue(2, 4)
    >>> fpq.enqueue(1, 64)
    >>> fpq.enqueue(0, 128)
    >>> print(fpq)
    Priority 0: [10, 100, 128]
    Priority 1: [70, 7, 64]
    Priority 2: [1, 5, 4]
    >>> fpq.dequeue()
    10
    >>> fpq.dequeue()
    100
    >>> fpq.dequeue()
    128
    >>> fpq.dequeue()
    70
    >>> fpq.dequeue()
    7
    >>> print(fpq)
    Priority 0: []
    Priority 1: [64]
    Priority 2: [1, 5, 4]
    >>> fpq.dequeue()
    64
    >>> fpq.dequeue()
    1
    >>> fpq.dequeue()
    5
    >>> fpq.dequeue()
    4
    >>> fpq.dequeue()
    Traceback (most recent call last):
        ...
    data_structures.queue.priority_queue_using_list.UnderFlowError: All queues are empty
    >>> print(fpq)
    Priority 0: []
    Priority 1: []
    Priority 2: []
    """
    def __init__(self) -> None:
        self.queue: list[list] = list(list(), list(), list())

    
    def enqueue(self, priority: int, data: Any) -> None:
        """
        Add data on priority basis
        If the priority is invalid ValueError raised.
        If the queue if full OverFlowError raised.
        """
        try:
            if len(self.queue[priority]) >= 100:
                raise  OverFlowError("Maximum queue size is 100")
            self.queue[priority].append(data)
        except IndexError:
            raise ValueError("Valid priorities are 0, 1, and 2")


    def dequeue(self) -> int:
        """
        Return the highest priority queue value.
        If queue is empty then an under flow exception raised.
        """
        for itr in self.queue:
            if itr:
                return itr.pop(0)
        raise UnderFlowError("All queue are empty")


    def __str__(self) -> str:
        return "\n".join(f"Priority {i}: {q}" for i, q in enumerate(self.queue))


class ElementPriorityQueue:
    """
    Element Priority Queue is the same as Fixed Priority Queue except that the value of
    the element itself is the priority. The rules for priorities are the same the as
    Fixed Priority Queue.

    >>> epq = ElementPriorityQueue()
    >>> epq.enqueue(10)
    >>> epq.enqueue(70)
    >>> epq.enqueue(4)
    >>> epq.enqueue(1)
    >>> epq.enqueue(5)
    >>> epq.enqueue(7)
    >>> epq.enqueue(4)
    >>> epq.enqueue(64)
    >>> epq.enqueue(128)
    >>> print(epq)
    [10, 70, 4, 1, 5, 7, 4, 64, 128]
    >>> epq.dequeue()
    1
    >>> epq.dequeue()
    4
    >>> epq.dequeue()
    4
    >>> epq.dequeue()
    5
    >>> epq.dequeue()
    7
    >>> epq.dequeue()
    10
    >>> print(epq)
    [70, 64, 128]
    >>> epq.dequeue()
    64
    >>> epq.dequeue()
    70
    >>> epq.dequeue()
    128
    >>> epq.dequeue()
    Traceback (most recent call last):
        ...
    data_structures.queue.priority_queue_using_list.UnderFlowError: The queue is empty
    >>> print(epq)
    []
    """
    def __init__(self) -> None:
        self.queue = list()
    

    def enqueue(self, data: Any) -> None:
        """
        In this function enters data on queue
        If queue is full then raise OverFlowError
        """
        if len(self.queue) == 100:
            raise OverFlowError("Queue has been fulled")
        self.queue.append(data)
    

    def dequeue(self) -> None:
        """
        In this funciton remove min value element
        If element not found in queue raise exception
        """
        if not self.queue:
            raise UnderFlowError("The queue is empty")
        else:
            element = min(self.queue)
            self.queue.remove(element)
            return element


    def __str__(self) -> str:
        return str(self.queue)

def fixed_priority_queue():
    fpq = FixedPriorityQueue()
    fpq.enqueue(0, 10)
    fpq.enqueue(1, 70)
    fpq.enqueue(0, 100)
    fpq.enqueue(2, 1)
    fpq.enqueue(2, 5)
    fpq.enqueue(1, 7)
    fpq.enqueue(2, 4)
    fpq.enqueue(1, 64)
    fpq.enqueue(0, 128)
    print(fpq)
    print(fpq.dequeue())
    print(fpq.dequeue())
    print(fpq.dequeue())
    print(fpq.dequeue())
    print(fpq.dequeue())
    print(fpq)
    print(fpq.dequeue())
    print(fpq.dequeue())
    print(fpq.dequeue())
    print(fpq.dequeue())
    print(fpq.dequeue())


def element_priority_queue():
    epq = ElementPriorityQueue()
    epq.enqueue(10)
    epq.enqueue(70)
    epq.enqueue(100)
    epq.enqueue(1)
    epq.enqueue(5)
    epq.enqueue(7)
    epq.enqueue(4)
    epq.enqueue(64)
    epq.enqueue(128)
    print(epq)
    print(epq.dequeue())
    print(epq.dequeue())
    print(epq.dequeue())
    print(epq.dequeue())
    print(epq.dequeue())
    print(epq)
    print(epq.dequeue())
    print(epq.dequeue())
    print(epq.dequeue())
    print(epq.dequeue())
    print(epq.dequeue())
