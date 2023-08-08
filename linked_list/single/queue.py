"""Queue using linked list."""
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
        self.head = self.rear = None
    
    def is_empty(self):
        """
        :intro: true if queue is empty, false else
        :rtype: bool
        """
        return self.head == None

    def enqueue(self, data):
        """
        :intro: append data in linked list.
        :data type: int
        :rtype: None
        """
        if not self.rear:
            self.head = self.rear = LinkedList(data)
            return
        self.rear.next = LinkedList(data)
        self.rear = LinkedList(data)
    
    def dequeue(self):
        """
        :intro: remove data starting point of the linked list.
        :rtype: None
        """
        if self.is_empty():
            return
        temp = self.head.next
        self.head.next = None
        self.head = temp

q = SingleLinkedList()
q.enqueue(10)
q.enqueue(20)
q.dequeue()
q.dequeue()
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.dequeue()
