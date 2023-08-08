# Push back

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

    def push_back(self, data):
        """
        :param data: value which store in back of the all node.
        :data type: int
        :rtype: Optinal[ListNode[prev, data, next]]
        """
        temp_node = ListNode(data)
        temp_node.prev = None
        if self.tail:
            self.tail.next = temp_node
            self.tail = temp_node
            self.tail.next = None
        else:
            self.head = self.tail = temp_node
            temp_node.next = None
        
    def display_back(self):
        """
        :rtype: None
        """
        curr = self.head
        while curr.next:
            print(curr.next.data)
            curr = curr.next

doublyLinkedList = DoublyLinkedList()
doublyLinkedList.push_back(1)
doublyLinkedList.push_back(2)
doublyLinkedList.push_back(3)
doublyLinkedList.push_back(4)
doublyLinkedList.push_back(5)
doublyLinkedList.display_back()
