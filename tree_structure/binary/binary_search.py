"""
- A rooted binary tree data structure with 
  the key of each internal node being greater 
  than all the keys in the respective node's 
  left subtree and less than the ones in 
  its right subtree.
- BST should be sorted.
"""
from __future__ import annotations

from dataclasses import dataclass

@dataclass
class TreeNode:
    data: int
    left: TreeNode = None
    right: TreeNode = None

    def insertion(self, data):
        """
        For inserting the data on tree.
        :data type: int
        :rtype: None
        """
        if self.data == data:
            return None
    
        if data < self.data:
            if self.left:
                return self.left.insertion(data)
            else:
                self.left = TreeNode(data)
                return None
        else:
            if self.right:
                return self.right.insertion(data)
            else:
                self.right = TreeNode(data)
                return None
