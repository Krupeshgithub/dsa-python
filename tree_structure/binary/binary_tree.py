"""
- A tree is called binary tree if each node of the tree has zero, one or two children.
- Empty tree is also a valid binary tree.
"""
from __future__ import annotations

from dataclasses import dataclass

@dataclass
class TreeNode:
    data: int
    left: TreeNode = None
    right: TreeNode = None

    def set_left(self, node):
        """
        For setting left node.
        :node type: List(TreeNode[data, left, right])
        :rtype: None
        """
        self.left = node
    
    
    def set_right(self, node):
        """
        For setting right node.
        :node type: List(TreeNode[data, left, right])
        :rtype: None
        """
        self.right = None
    
    
    def get_left(self):
        """
        For getting right node.
        :rtype: List(TreeNode[data, left, right])
        """
        return self.left

    
    def get_right(self):
        """
        For getting left node.
        :rtype: List(TreeNode[data, left, right])
        """
        return self.right

    
    def get_data(self):
        """
        For getting data of a node.
        :rtype: None
        """
        return self.data

    
    def inorder(self, tree):
        """
        left -> data -> right
        :tree type: List(TreeNode[data, left, right])
        :rtype: None
        """
        if tree:
            self.inorder(tree.get_left())
            print(tree.get_data(), end=' ')
            self.inorder(tree.get_right())
        return None
    
    
    def preorder(self, tree):
        """
        data -> left -> right
        :tree type: List(TreeNode[data, left, right])
        :rtype: None
        """
        if tree:
            print(tree.get_data(), end = ' ')
            self.preorder(tree.get_left())
            self.preorder(tree.get_right())
        return None

    
    def postorder(self, tree):
        """
        left -> right -> data
        :tree type: List(TreeNode[data, left, right])
        :rtype: None
        """
        if tree:
            self.preorder(tree.get_left())
            self.preorder(tree.get_right())
            print(tree.get_data(), end = ' ')
        return None


root = TreeNode(1)
root.set_left(TreeNode(2))
root.set_right(TreeNode(3))
root.left.set_left(TreeNode(4))

root.inorder(root)
root.preorder(root)
root.postorder(root)
