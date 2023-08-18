"""
BFT: Breadth-first traversal
Zig-zag traversal with level wise.
"""
from __future__ import annotations

import collections

from dataclasses import dataclass


@dataclass
class TreeNode:
    data: int
    left: TreeNode = None
    right: TreeNode = None


def make_tree():
    """
    For creating tree.
    :rtype: List[TreeNode[left, right, data]]
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(7)
    return root


def zigzag_straight(tree):
    """
    ZigZag traverse by iterative method: 
    Print node left to right and right to left, 
    alternatively.
    :tree type: List[TreeNode[left, right, data]]
    :rtype: None
    """
    if tree is None:
        return None

    queue = collections.deque([tree])
    flag = True  # left -> right
    res = []
    while queue:
        temp = []
        for _ in range(len(queue)):
            if flag:
                node = queue.popleft()
                temp.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                node = queue.pop()
                temp.append(node.data)
                if node.right:
                    queue.appendleft(node.right)
                if node.left:
                    queue.appendleft(node.left)
        flag = not flag
        res.append(temp)
    print(res)
    return res


def zigzag_straight_with_res(tree):
    """
    First we will append all data in res,
    Then we will modify res as per zigzag.
    :tree type: List[TreeNode[left, right, data]]
    :rtype: None
    """
    if tree is None:
        return None
    
    queue = collections.deque([tree])
    res = list()
    while queue:
        temp = list()
        for _ in range(len(queue)):
            node = queue.popleft()
            temp.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(temp)

    return [
        itr2[::-1] 
        if (itr1 % 2) == 0 
        else itr2 
        for itr1, itr2 in enumerate(res)
    ]


def zigzag_stack(tree):
    """
    For this function store tree on stack.
    :tree type: List[TreeNode[left, right, data]]
    :rtype: None
    """
    if tree is None:
        return None
    
    res = list()
    stack = [tree]
    flag = True
    while stack:
        temp = list()
        temp_stack = list()
        for _ in range(len(stack)):
            node = stack.pop()
            temp.append(node.data)
            if flag:
                if node.left:
                    temp_stack.append(node.left)
                if node.right:
                    temp_stack.append(node.right)
            else:
                if node.right:
                    temp_stack.append(node.right)
                if node.left:
                    temp_stack.append(node.left)
        res.append(temp)
        flag = not flag
        stack = temp_stack
    return res


root = make_tree()
zigzag_straight(root)
zigzag_straight_with_res(root)
zigzag_stack(root)
