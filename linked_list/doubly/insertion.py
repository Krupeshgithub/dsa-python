"""Doubly linked list insertion process."""

class LinkedList:
    def __init__(self, data):
        """
        :intro: constructor to create node with prev and next node address.
        :param data: add data on data.
        :data type: int
        :rtype: Optional[prev, data, next]
        """
        self.prev = None
        self.data = data
        self.next = None
    
class DoublyLinkedList:

    def __init__(self):
        """
        :intro: constructor store linked node.
        :rtype: Optional[List[prev, data, next]]
        """
        self.head = None
    
    def insert_at_start(self, data):
        """
        :intro: insert an element at the beginning of the linked list.
        :data type: int
        :rtype: None
        """
        if self.head:
            new_node = LinkedList(data)
            self.head.prev = self.head = new_node
            new_node.next = self.head
        else:
            self.head = LinkedList(data)

    def insert_at_end(self, data):
        """
        :intro: insert an element at the end of the linked list.
        :data type: int
        :rtype: None
        """
        new_node = LinkedList(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_start(1)
    dll.insert_at_start(2)
    dll.insert_at_start(3)
    dll.insert_at_start(4)
    dll.insert_at_start(5)
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_at_end(4)
    dll.insert_at_end(5)
