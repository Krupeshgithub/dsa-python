'''
PostOrderVetex: 

          a
         / \    
        b   c
        
        pre_order_vertex:  [left, right, root] -> [b, c, a]
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
            
    # Post-order traversal 
    # left -> right -> root
    def post_order_traversal(self, vertex):
        lst = []
        if vertex:
            lst = lst + self.post_order_traversal(vertex.left)
            lst = lst + self.post_order_traversal(vertex.right)
            lst.append(vertex.data)
        return lst
        
vertex = Node(27)
vertex.insert(14)
vertex.insert(35)
vertex.insert(10)
vertex.insert(19)
vertex.insert(31)
vertex.insert(42)
print(vertex.post_order_traversal(vertex))
