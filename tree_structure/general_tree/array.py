#!/usr/bin/env python3
"""
General tree which store n-numbers of the child.
Implement general tree with array
"""
from __future__ import annotations

from typing import Any

from dataclasses import dataclass


@dataclass
class Node:
    """
    Implement node which store key and array of the childs
    """
    key: Any = None
    child: Any | None = list()


class GeneralTree:
    """
    General tree with level order traversal (BFS)
    """


    def temp_node(self, data: Any) -> Node:
        """
        >>> gt = GeneralTree()
        >>> gt.temp_node(data)
        <__main__.Node object at 0x7f3a6c7bdf70>
        """
        return Node(data)


    def level_order_traversal(self, root: Node) -> None:
        """
        >>> gt = GeneralTree()
        >>> root_node = gt.temp_node(10)
        >>> (root_node.child).append(Node(2))
        >>> (root_node.child).append(Node(34))
        >>> (root_node.child).append(Node(56))
        >>> (root_node.child).append(Node(100))
        >>> (root_node[0].child).append(Node(77))
        >>> (root_node[0].child).append(Node(88))
        >>> (root_node[2].child).append(Node(1))
        >>> (root_node[3].child).append(Node(7))
        >>> (root_node[3].child).append(Node(8))
        >>> (root_node[3].child).append(Node(9))
        >>> gt.level_order_traversal(root_node)
        10
         | ----- 2
                 | ----- 77
                 | ----- 78
         | ----- 34
         | ----- 56
                 | ----- 1
         | ----- 100
                 | ----- 7
                 | ----- 8
                 | ----- 9
        
        >>> root is None
        Traceback (most recent call last):
        ...
        Exception: `Empty root not avaliable`
        """

        assert not root, "Empty root not avaliable"

        