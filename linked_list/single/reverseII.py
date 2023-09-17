"""
Reverse linked list with specify position.

i.e.
    1-2-3-4-5
    1-4-3-2-5
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LinkedList:
    """
    Initialize node which store data and next
    node address.

    :rtype: Object[data, next]
    """
    data: int
    next: object[list] = None


@dataclass
class SingleLinkedList:
    """
    Present head of the node.
    """
    head: object[list] = None


    def insert(self, lst):
        """
        Create linkeslist with all data which given
        in list to the node.

        :type lst: List
        :rtype: None
        """
        for itr in lst:
            if self.head:
                curr = self.head
                while curr.next:
                    curr = curr.next
                curr.next = LinkedList(itr)
            else:
                self.head = LinkedList(itr)


    def reverse(self, head, steps):
        """
        Revese linked list to specific position.

        :type steps: int
        :rtype: None
        """
        count = 0
        curr = head
        prev = None
        while count < steps:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1


    def reverseII(self, left, right):
        """
        Reverse linked list with specific position
        and return whole linked list.

        :type left: int
        :type right: int
        :rtype: Object[List]
        """
        prev_left = left_node = right_node = None
        curr = self.head

        for itr in range(1, right+1):
            if itr == (left-1):
                prev_left = curr
            elif itr == left:
                left_node = curr
            elif itr == right:
                right_node = curr
            curr = curr.next
        
        next_right = right_node.next
        self.reverse(head=left_node, steps=(right-left+1))
        self.reverse(
            head=left_node,
            steps=(right-left+1)
        )
        left_node.next = next_right

        if prev_left:
            prev_left.next = right_node
            return self.head
        else:
            return right_node


    def pprint(self):
        """
        Present current head of the linked list.

        :rtype: None
        """
        if self.head:
            curr = self.head
            while curr:
                print(curr.data)
                curr = curr.next


sll = SingleLinkedList()
sll.insert([1, 2, 3, 4, 5])
sll.reverseII(2, 4)
sll.pprint()
