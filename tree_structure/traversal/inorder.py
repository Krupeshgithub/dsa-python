'''
PreOrderVertex: 

          a
         / \    
        b   c
        
        pre_order_vertex:  [left, root, right] -> [b, a, c]
'''

class Node:
    
    def __init__(self, data) -> int:
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data) -> int:
        
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif self.data < data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
        
    def printTree(self) -> None:
        if self.left:
            self.left.printTree()
        print(self.data, )
        if self.right:
            self.right.printTree()
            
    # In-order traversal 
    # left -> root -> right
    def in_order_traversal(self, vertex):
        lst = []
        if vertex:
            lst = lst + self.in_order_traversal(vertex.left)
            lst.append(vertex.data)
            lst = lst + self.in_order_traversal(vertex.right)
        return lst
        
vertex = Node(27)
vertex.insert(14)
vertex.insert(35)
vertex.insert(10)
vertex.insert(19)
vertex.insert(31)
vertex.insert(42)
print(vertex.in_order_traversal(vertex))
