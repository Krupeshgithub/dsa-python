**Tree**

* A tree is a data structure similar to a linked List but instead of each node pointing simply to the next node in a linear fashion, each node points to a number of nodes. Tree is an example of non-linear data structures. A tree structure is a way of representing the **hierarchical** nature of a structure in a graphical form.
* The **root** of the tree is the node with no parents. There can be at most one root node in a tree.
* The _edge_ refers to the link from parent to child.
* A node with NO children is called _leaf_ node.
* Children of same parent are called _siblings_.


**Type of binary tree**

- No ordered

> Time complexity: O(n)

1. **Full binary tree**:
    A Binary Tree is full if every node has 0 or 2 children. Following are examples of full binary tree.
2. **Complete binary tree**:
    A Binary Tree is complete Binary Tree if all levels are completely filled except possibly the last level and the last level has all keys as left as possible.
3. **Perfect Binary Tree**:
    A Binary tree is Perfect Binary Tree in which all internal nodes have two children and all leaves are at same level.
4. **Balanced Binary Tree**:
    A binary tree is balanced if height of the tree is O(Log n) where n is number of nodes. For Example, AVL tree maintain O(Log n) height by making sure that the difference between heights of left and right subtrees is 1. Red-Black trees maintain O(Log n) height by making sure that the number of Black nodes on every root to leaf paths are same and there are no adjacent red nodes. Balanced Binary Search trees are performance wise good as they provide O(log n) time for search, insert and delete.
5. **A degenerate (or pathological) tree**:
    A Tree where every internal node has one child. Such trees are performance-wise same as linked list.

**Type of binary search tree**

- Ordered

> Time complexity: O(log n)

***Properties***

1. All nodes of left subtree are less than the root node
2. All nodes of right subtree are more than the root node
3. Both subtrees of each node are also BSTs i.e. they have the above two properties

***Types***

```
AVL Trees
Splay Trees
Tango Trees
T-Trees
Red-Black Trees
```
