#!/usr/bin/env python3
"""
Implementation of Circular Queue using linked lists
"""
from __future__ import annotations

from typing import DefaultDict


class CircularQueueLinkedList:
    """
    Circular FIFO list with the given capacity (default queue length: 6)

    >>> cq = CircularQueueLinkedList(2)
    >>> cq.enqueue('a')
    >>> cq.enqueue('b')
    >>> cq.enqueue('c')
    Traceback (most recent call last):
        ...
    Exception: `Full Queue`
    """


    def __init__(self, initial_capacity=6):
        """
        Initialize front, rear and impliment linked list

        :type initial_capacity: int
        :rtype: None
        """
        self.front = None
        self.rear = None
        self.create_linked_list(initial_capacity)
        

    def create_linked_list(self, initial_capacity):
        """
        Impliment linked list with initial capacity

        :type initial_capacity: int
        :rtype: None
        """
        curr = Node()
        self.front = curr
        self.rear = curr
        prev = curr
        for _ in range(initial_capacity-1):
            curr = Node()
            prev.next = curr
            curr.prev = prev
            prev = curr
        prev.next = self.front
        self.front.prev = prev


    def is_empty(self):
        """
        Checks where the queue is empty or not
        >>> cq = CircularQueueLinkedList()
        >>> cq.is_empty()
        True
        >>> cq.enqueue('a')
        >>> cq.dequeue()
        'a'
        >>> cq.is_empty()
        True

        :rtype: None
        """
        return (
            self.front == self.rear
            and self.front is not None
            and self.front.data is None
        )


    def first(self):
        """
        Returns the first element of the queue

        >>> cq = CircularQueueLinkedList()
        >>> cq.first()
        Traceback (most recent call last):
         ...
        Exception: `Empty Queue`
        >>> cq.enqueue('a')
        >>> cq.first()
        'a'
        >>> cq.dequeue()
        'a'
        >>> cq.first()
        Traceback (most recent call last):
         ...
        Exception: `Empty Queue`
        >>> cq.enqueue('b')
        >>> cq.enqueue('c')
        >>> cq.first()
        'b'
        """
        self.check_operation()
        return self.front.data if self.front else None


    def enqueue(self, data):
        """
        Saves data at the end of the queue

        >>> cq = CircularQueueLinkedList()
        >>> cq.enqueue('a')
        >>> cq.enqueue('b')
        >>> cq.dequeue()
        'a'
        >>> cq.dequeue()
        'b'
        >>> cq.dequeue()
        Traceback (most recent call last):
           ...
        Exception: `Empty Queue`

        :type data: int
        :rtype: None
        """
        if self.rear is None:
            return

        self.check_is_full()
        if not self.is_empty():
            self.rear = self.rear.next
        if self.rear:
            self.rear.data = data


    def dequeue(self):
        """
        Removes and retrieves the first element of the queue

        >>> cq = CircularQueueLinkedList()
        >>> cq.dequeue()
        Traceback (most recent call last):
           ...
        Exception: `Empty Queue`
        >>> cq.enqueue('a')
        >>> cq.dequeue()
        'a'
        >>> cq.dequeue()
        Traceback (most recent call last):
           ...
        Exception: `Empty Queue`

        :rtype: None
        """
        self.check_operation()
        if (
            not self.rear
            or not self.front
        ):
            return
        if self.front == self.rear:
            data = self.front.data
            self.front.data = None
            return data

        temp = self.front
        self.front = temp.next
        data = temp.data
        temp.data = None
        return data
    

    def check_operation(self):
        """
        Check the queue is empty or not

        :rtype: None | assert
        """
        assert not self.is_empty(), "Empty Queue"


    def check_is_full(self):
        """
        Check the queue is full or not

        :rtype: None | assert
        """
        assert (
            self.rear
            and self.rear.next == self.front
        ), "Full Queue"


class Node:
    """
    Initialize linked list node
    """

    def __init__(self):
        """
        Dounbly linked list
        prev, data, next
        """
        self.prev: Node[DefaultDict] = None
        self.data: int = None
        self.next: Node[DefaultDict] = None


cq = CircularQueueLinkedList(6)
cq.enqueue('a')
cq.enqueue('b')
cq.dequeue()
cq.dequeue()
cq.first()
