"""Rotate single linked list at per position given."""

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
    
    def rotate(self, position):
        """
        :intro: start liked list at given postion if 
                postion not found then position not change.
        :position type: int
        :rtype: Optional[List[data, next]]
        """
        curr = self.head
        count = 0
        if position == count:
            return self.head

        while (position != count \
            and curr):
            curr = curr.next
            count+=1

        if not curr:
            return self.head

        temp = curr

        while curr.next:
            curr = curr.next
        
        curr.next = self.head
        self.head.next = temp.next
        temp.next = None
        return (curr)

sll = SingleLinkedList()
sll.insert([1, 2, 3, 4, 5])
sll.rotate(2)
