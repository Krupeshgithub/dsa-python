"""
We continuosuly remove the smallest element from the
unsorted element and append into first of the array.

illustration,
li = [5, 9, 1, 6]

first = [5, 9, 1, 6] is 5 > 9 ? No
second = [5, 1, 9, 6] is 9 > 1 ? Yes
thired =  [5, 1, 6, 9] is 9 > 6 ? Yes
forth = [1, 5, 6, 9] is 5 > 1 ? Yes
fifth = [1, 5, 6, 9] is 5 > 6 ? No
six = [1, 5, 6, 9] is 6 > 9 ? No
seven = [1, 5, 6, 9] is 1 > 5 ? No
eight = [1, 5, 6, 9] is 5 > 6 ? No
nine = [1, 5, 6, 9] is 6 > 9 ? 


Time Complexity: O(n^2)
Space Complexity: O(1)
"""



class LinkedNode:
    def __init__(self, data):
        """
        :intro: create a node which store data and next node pointer.
        :data type: int
        :rtype: LinkedNode[List[data, next]]
        """
        self.data = data
        self.next = None


class SingleLinkedNode:
    def __init__(self):
        """
        Store multiple nodes in linked.
        :rtype: LinkedNode[List[data, next]]
        """
        self.head = None


    def insert(self, lst):
        """
        Insert all data which given in list to the node.
        :type lst: List
        :rtype: None
        """
        for itr in lst:
            if self.head:
                curr = self.head
                while curr.next:
                    curr = curr.next
                curr.next = LinkedNode(itr)
            else:
                self.head = LinkedNode(itr)


    def insertion_sort(self):
        """
        Change position if `prev nodes > head`, else continue.
        :rtype: LinkedNode[List[data, next]]
        """ 
        pointer = self.head
        curr = self.head.next
        while curr:
            while (
                pointer.data > curr.data
                and (curr != None) 
            ):
                pointer = pointer.next
            pointer.next = curr.next
            curr.next = pointer            
            curr = curr.next
        print(curr, self.head)

sll = SingleLinkedNode()
sll.insert([4, 3, 2, 10, 12, 1, 5, 6])
sll.insertion_sort()
