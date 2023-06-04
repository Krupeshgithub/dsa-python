'''Create a node and store insert left or right node.

Node/Vertex: Node always store 3 parameters. 
1) Data
2) Left node
3) Right node
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
            
vertex = Node(27)
vertex.insert(14)
vertex.insert(35)
vertex.insert(10)
vertex.insert(19)
vertex.insert(31)
vertex.insert(42)
vertex.printTree()
