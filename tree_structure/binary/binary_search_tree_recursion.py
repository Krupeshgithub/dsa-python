#!/usr/bin/env python3
"""
A binary search tree ( Recursion Method )

Example:
              8
             / \
            3   10
           / \    \
          1   6    14
             / \   /
            4   7 13

Rule: To impliment binary search tree lowest 
      element to root will build in left and 
      highest element to root will build in right.

Pre-Order: [8, 3, 1, 6, 4, 7, 10, 14, 13]
In-Order: [1, 3, 6, 4, 7, 8, 10, 14, 13]
Post-Order: [1, 3, 6, 4, 7, 13, 14, 10, 8]
Breadth-First: [8, 3, 10, 1, 6, 14, 4, 7, 13]

>>> bst = BinarySearchTree()
>>> bst.insert(8, 3, 6, 1, 10, 14, 13, 4, 7)
>>> print(" ".join(repr(itr) for itr in bst.travel_tree()))
8, 3, 1, 6, 4, 7, 10, 14, 13
>>> bst.remove(26)
Traceback (most recent call last):
    ...
ValueError: Value 20 not found
>>> BinarySearchTree().search(6)
Traceback (most recent call last):
    ...
IndexError: Warning: Tree is empty! please use another.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, DefaultDict


@dataclass(repr=False)
class BinarySearchTree:
    """
    Initialize node which has store data, left child node object,
    and right child node object.
    """
    data: int | Any
    left: None | object[DefaultDict] = None
    right: None | object[DefaultDict] = None
    min: None | int = None
    max: None | int = None


    def __repr__(self) -> str:
        from pprint import pformat

        if not self.left and not self.right:
            return str(self.data)
        return pformat({f"{self.data}": (self.left, self.right)}, indent=1)


    def insert(self, data: int) -> None:
        if self.data == data:
            return
        
        if self.data > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BinarySearchTree(data)


    def in_order(self, lst: list(int)=[]) -> list[int]:
        """
        Left -> Root -> Right
        """
        if self.data:
            if self.left:
                self.left.in_order(lst)
            lst.append(self.data)
            if self.right:
                self.right.in_order(lst)
        return lst

    
    def pre_order(self, lst: list(int)=[]) -> list(int):
        """
        Root -> Left -> Right
        """
        if self.data:
            lst.append(self.data)
            if self.left:
                self.left.pre_order(lst)
            if self.right:
                self.right.pre_order(lst)
        return lst


    def post_order(self, lst: list(int)=[]) -> list(int):
        """
        Left -> Right -> Root
        """
        if self.data:
            if self.left:
                self.left.post_order(lst)
            if self.right:
                self.right.post_order(lst)
            lst.append(self.data)
        return lst


    def search(self, data: int) -> bool:
        """If data in tree return true, else false"""
        assert self.data, "Tree not found"
        if self.data == data:
            return True

        if self.data < data:
            if self.right:
                return self.right.search(data)
        elif self.data > data:
            if self.left:
                return self.left.search(data)
        return False


    def get_min(self) -> int:
        if not self.left:
            return self.data
        return self.left.get_min()


    def delete(self, data: int) -> None:
        """
        Delete element if exist, else return none
        """
        assert self.data, "Element not found"

        if self.data > data:
            if self.left:
                self.left.delete(data)
        elif self.data < data:
            if self.right:
                self.right.delete(data)
        else:
            if not self.left and not self.right:
                return

            if not self.left and self.right:
                return self.right

            min_val = self.right.get_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        print(self)
        return self


bst = BinarySearchTree(10)  
bst.insert(8)
bst.insert(20)
bst.insert(60)
bst.insert(70)
bst.insert(1)
bst.delete(70)
print(bst.in_order())
