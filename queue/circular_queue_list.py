#!/usr/bin/env python3
"""Implement of Circular Queue using python list"""
from __future__ import annotations

from typing import Any

class CircularQueue:
    """Circular FIFO queue with a fixed capacity"""

    def __init__(self, number: int=5):
        self.number: int = number
        self.queue: list[Any] = [None] * self.number
        self.front: None | int = None
        self.rear: None | int = None
        self.size: None | int = None

    
    def __len__(self):
        """
        >>> cq = CircularQueue(5)
        >>> len(cq)
        0
        >>> cq.enqueue("A")
        <data_structures.queue.circular_queue.CircularQueue object at ...
        >>> len(cq)
        1
        """
        return self.size


    def is_empty(self):
        """
        >>> cq = CircularQueue(5)
        >>> cq.is_empty()
        True
        >>> cq.enqueue("A").is_empty()
        False
        """
        return self.size == 0
    

    def first(self):
        """
        >>> cq = CircularQueue(5)
        >>> cq.first()
        False
        >>> cq.enqueue("A").first()
        'A'
        """
        return False if self.is_empty() else self.queue[self.front]
    

    def enqueue(self, value: int):
        """
        This function insert an element in the queue using self.rear value as an index
        >>> cq = CircularQueue(5)
        >>> cq.enqueue("A")  # doctest: +ELLIPSIS
        <data_structures.queue.circular_queue.CircularQueue object at ...
        >>> (cq.size, cq.first())
        (1, 'A')
        >>> cq.enqueue("B")  # doctest: +ELLIPSIS
        <data_structures.queue.circular_queue.CircularQueue object at ...
        >>> (cq.size, cq.first())
        (2, 'A')
        """
        assert not (self.size >= self.number), "QUEUE IS FULL"

        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.number
        self.size += 1
        return
    

    def dequeue(self):
        """
        This function removes an element from the queue using on self.front value as an
        index
        >>> cq = CircularQueue(5)
        >>> cq.dequeue()
        Traceback (most recent call last):
           ...
        Exception: UNDERFLOW
        >>> cq.enqueue("A").enqueue("B").dequeue()
        'A'
        >>> (cq.size, cq.first())
        (1, 'B')
        >>> cq.dequeue()
        'B'
        >>> cq.dequeue()
        Traceback (most recent call last):
           ...
        Exception: UNDERFLOW
        """
        assert self.size != 0, "UNDERFLOW"

        temp = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.number
        self.size -= 1
        return temp


cq = CircularQueue(6)
cq.enqueue('a')
cq.enqueue('b')
cq.dequeue()
cq.dequeue()
cq.first()
