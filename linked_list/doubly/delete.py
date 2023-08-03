"""Doubly linked list delete process."""

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

    def delete(self, data):
        """
        :intro: to delete specified element from the linked list.
        :data type: int
        :rtype: bool
        """
        temp = self.head
        if temp.next:
            if temp.data == data:
                self.head = temp.next
                temp.next.prev = temp.next = None
                return True
            else:
                while temp.data == data or temp.next:
                    temp = temp.next
                if temp.next:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    temp.prev = temp.next = None
                else:
                    temp.prev.next = temp.prev = None
        if not temp:
            return False            

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_at_end(4)
    dll.insert_at_end(5)
