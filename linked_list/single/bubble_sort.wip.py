"""Bubble sort useing linked list."""
class LinkedList:
    def __init__(self, data):
        """
        :intro: create a node which store data and next node address.
        :data type: int
        :rtype: Optional[data, next]
        """
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        """
        :intro: store multiple nodes in linked.
        :rtype: Optional[List[data, next]]
        """
        self.head = None
    
    def insert(self, lst):
        """
        :intro: insert all data which given in list to the node.
        :lst type: List
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
        
    def bubble_sort(self):
        """
        :intro: sort linked list with help of bubble sort algo.
        :rtype: Optinal[LinkedList] if self.head, else None.
        """
        if not self.head:
            return
        
        swapped = True
        while swapped:
            curr = self.head
            swapped = False
            prev = None
            while (curr.next):
                if curr.data > curr.next.data:
                    print(curr.data)
                    prev = curr.next
                    temp = curr.next.next
                    curr.next.next = curr
                    curr.next = temp
                    swapped = True
                else:
                    print(curr.data)
                    curr = curr.next
        return self.head

sll = SingleLinkedList()
sll.insert([5, 9, 1, 6])
sll.bubble_sort()
