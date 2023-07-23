'''
For method annotations.
'''
from typing import (Optional, List, 
                    AnyStr, Any,
                    NoReturn, Dict)


class Node:
    def __init__(self, data: int) -> Optional[List]:
        '''Linked list node consume data and next node address.'''
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self) -> None:
        '''Node current head.'''
        self.head = None
    
    def insertion(self, lst: List[int]) -> Optional[Dict]:
        '''Get list of integer values and store every node and return object.'''
        for itr in lst:
            if (self.head):
                current = self.head
                while current.next:
                    current = current.next
                current.next = Node(itr)
            else:
                self.head = Node(itr)
    
    def representList(self) -> None:
        '''Show all node values in linked list.'''
        current = self.head
        while current:
            print(current.data)
            current = current.next        

linkedList = LinkedList()
linkedList.insertion([1, 2, 3, 4, 5])
linkedList.representList()
