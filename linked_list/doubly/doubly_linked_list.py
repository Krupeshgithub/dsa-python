class ListNode:
    def __init__(self, data):
        """
        :intro: return pair of the node.

        :param data: data be store in the node.
        :data type: int
        :rtype: defaultdict[prev, data, next]
        """
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        """
        :intro: return head of the node.

        :rtype: defaultdict[prev, data, next]
        """
        self.head = None

    def insert_at_front(self, data):
        """
        :intro: insert an element at the beginning of the linked list.

        :param data: insert data in node and node be joint at beginning of the node.
        :data type: int
        :rtype: none
        """
        if not self.head:
            self.head = ListNode(data)
        else:
            temp_node = ListNode(data)
            self.head.prev = temp_node
            temp_node.next = self.head
            self.head = temp_node

    def insert_at_back(self, data):
        """
        :intro: insert an element at the back of the linked list.

        :param data: insert data in node and node be joint at back of the node.
        :data type: int
        :rtype: none
        """
        new_node = ListNode(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def delete(self, data):
        """
        :intro: delete node at any position of the linked list.

        :param data: to delete specified element from the linked list.
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
                while temp.next or temp.data == data:
                    temp = temp.next
                if temp.next:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    temp.next = temp.prev = None
                else:
                    temp.prev.next = temp.next = None
        else:
            return False
        
    def get_data(self, data):
        """
        :intro: return doubly linked list data.

        
        """

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_at_front(1)
    dll.insert_at_front(2)
    dll.insert_at_front(3)
