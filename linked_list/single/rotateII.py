"""
RotateII linked list.
Ex:
    HEAD = 1 -> 2 -> 3 -> 4
    RETURN HEAD = 1 -> 4 -> 2 -> 3

Theory: L0, L1, L2, ..... , L(n-1), L(n)
        L0, L(n), L1, L(n-1), .....

"""
import copy

class LinkedNode:
    def __init__(self, data):
        """
        Create node and store data and next pointer address.
        :data type: int
        :rtype: None
        """
        self.data = data
        self.next = None

class RotateII:
    def __init__(self):
        """
        Head of the created linked list.
        :rtype: None
        """
        self.head = None
        self.rev = None
        self.length = 0

    def insert(self, data):
        """
        Insert data in to node and linked with head next pointer.
        :data type: int
        :rtype: None
        """
        temp = LinkedNode(data)
        if self.head:
            curr = self.head
            while (curr.next):
                curr = curr.next
            curr.next = temp
        else:
            self.head = temp
        return None
    
    def reverse(self):
        """
        Reverse head which store chain of the nodes.
        :rtype: None
        """
        self.rev = copy.deepcopy(self.head)
        curr = self.rev
        prev = None
        follower = curr.next
        length = 0
        while curr:
            curr.next = prev
            prev = curr
            curr = follower
            if follower:
                follower = follower.next
            length += 1
        self.rev = prev
        self.length = length - 1

    def rotate(self):
        """
        Rotate head with L0, L(n), L1, ...
        :rtype: List(LinkedNode[data, next])
        """
        head = self.head
        tail = self.rev
        count = 0
        new_head = None
        while head.next:
            if (count % 2) == 0:
                temp = head
                head = head.next
                temp.next = None
                if new_head is None:
                    new_head = temp
                else:
                    new_head = temp
            else:
                temp = tail
                tail = tail.next
                temp.next = None
                new_head = temp
            if self.length == count:
                break
            count += 1
            new_head = new_head.next
        return new_head

rotateLL = RotateII()
rotateLL.insert(1)
rotateLL.insert(2)
rotateLL.insert(3)
rotateLL.insert(4)
rotateLL.reverse()
rotateLL.rotate()
