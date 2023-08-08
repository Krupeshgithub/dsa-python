# Push front

class ListNode:
    def __init__(self, data):
        """
        :param data: value given which store in node.
        :data type: int
        :rtype: Optional[ListNode[prev, data, next]]
        """
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        """
        :rtype: Optional[ListNode[prev, data, next]]
        """
        self.head = None
        self.tail = None

    def push_front(self, data):
        """
        :param data: value which store in front of the all node.
        :data type: int
        :rtype: Optional[ListNode[prev, data, next]]
        """
        temp_node = ListNode(data)
        temp_node.next = None
        if self.head:
            self.head.prev = temp_node
            self.head = temp_node
            self.head.next = None
        else:
            self.head = self.tail = temp_node
            temp_node.prev = None
        
    def pop_front(self):
        """
        :rtype: Optional[ListNode[prev, data, next]]
        """
        if not self.tail:
            return

        temp = self.tail
        temp.prev.next = None
        self.tail = temp.prev
        temp.prev = None
        return temp.data

doublyLinkedList = DoublyLinkedList()
doublyLinkedList.push_front(1)
doublyLinkedList.push_front(2)
doublyLinkedList.push_front(3)
doublyLinkedList.push_front(4)
doublyLinkedList.push_front(5)
doublyLinkedList.pop_front()
