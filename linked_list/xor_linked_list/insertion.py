""" xor linked list insertion functionality. """
import ctypes

class ListNode:
    def __init__(self, data):
        """
        :intro: Create node which store data and 
                xor pointer.
        :data type: int
        :rtype: int
        """
        self.data = data
        self.npx = 0

class XorLinkedList:
    def __init__(self):
        """
        :intro: Store xor linked list at head poistion.
        :rtype: None
        """
        self.head = self.tail = None    

    def insertion(self, data):
        """
        :intro: Create node chain which store data and
                npx of the data.
        :data type: int
        :rtype: None
        """
        node = ListNode(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.head.npx = id(node) ^ self.head.npx
            node.npx = id(self.head)
            self.head = node

    def display(self):
        """
        :intro: Display all node data.
        :rtype: None
        """
        if not self.tail:
            return ("ListNode node found!")
        prev = 0
        curr = self.tail
        _next = 1
        while _next:
            _next = prev ^ curr.npx
            print(_next)
            if _next:
                prev = id(curr)
                curr = ctypes.cast(_next, ctypes.py_object).value
                print(curr.data, end=" ")
            else:
                return

    def __type_cast(self, index):
        """
        :intro: Method to return new instance of type.
        :index type: ID
        :rtype: None
        """
        return ctypes.cast(index, ctypes.py_object).value

xor = XorLinkedList()
xor.insertion(2)
xor.insertion(3)
xor.insertion(4)
xor.insertion(5)
xor.display()
