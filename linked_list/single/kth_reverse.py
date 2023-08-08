"""Reverse linked list with kth first and second both 
linked list."""
class ListNode:
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
                curr.next = ListNode(itr)
            else:
                self.head = ListNode(itr)
    
    def reverse(self, linked_list):
        """
        :intro: reverse linked list.
        :linked_list type: Optional[ListNode]
        :rtype: reverse(Optional[ListNode])
        """
        prev = None
        curr = self.head
        follower = curr.next
        while follower:
            curr.next = prev
            prev = curr
            curr = follower
            if follower:
                follower = follower.next
        return prev

    def kth_reverse(self, k):
        """
        :intro: reverse starting and ending of the 
                kth position linked list. If the not 
                len(linked_list)%2 is zero then cosider 
                kth postition of the node.
        :k type: int
        :rtype: Optional[ListNode]
        """
        curr = self.head
        count = 0
        while count == k:
            curr = curr.next
