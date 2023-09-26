***Overview***

- Data structures and algorithms form the basic foundation of computer science. While data structures tell us how the data will be stored, algorithms provide us with an efficient way to store it.

**What is tree data structure?**

- A tree is a hierarchical data structure made up of nodes. These nodes contain data and have zero or more child nodes, and each child node has one parent node (except for the root node, which has no parent).

- Trees are commonly used to represent hierarchical relationships, such as the file system on a computer. The topmost node is called the root of the tree, and the bottommost nodes are called the leaves of the tree.

**Terminology**

1 Root: The topmost node in the tree.
 
2 Child: A node that is directly connected to another node (its parent).
 
3 Parent: A node that has one or more child nodes.
 
4 Leaf: A node that has no children.
 
5 Sibling: Nodes that share the same parent.
 
6 Ancestor: A node higher in the tree and connected to the node by following the parent pointers.
 
7 Descendant: A node lower in the tree and connected to the node by following the child pointers.
 
8 Subtree: A tree that consists of a node and all its descendants.
 
9 Depth: The distance between a node and the root of the tree.
 
10 Height: The distance between a node and its furthest descendant leaf node.
 
11 Level: Count of edges on the path from a node to the root node.
 

**Applications**

1 File systems: Trees are used to organize and store files in a hierarchical structure.
 
2 Decision-making: Trees are used to model decision-making processes, where each node represents a decision point, and each branch represents a possible outcome.
 
3 Expression parsing: Trees are used to represent mathematical expressions and can be used to evaluate them.
 
4 Huffman coding: Trees are used to compress data by representing frequently occurring data with shorter codes and less frequent data with longer codes.
 
5 Graph algorithms: Many graph algorithms, such as depth-first search and breadth-first search, are implemented using tree data structures.
 
6 Artificial Intelligence: Decision Trees and Random Forest are used in machine learning and AI as models.
 
7 Database indexing: Trees are used to index and organize data in databases for faster retrieval.
 
8 Network routing protocols: Trees are used to organize and optimize communication networks.
 
9 Compiler Design: Syntax trees are used in compilers to represent the syntactic structure of a program.
 
10 Game AI: Game AI often uses tree data structures to model game states and possible moves in a game and to evaluate them using game-specific metrics.

**Types**

```
General tree
Binary tree
Binary search tree
Balanced tree
complete tree
full tree
Perfect tree
AVL tree
Red-Black tree
Heap
```

**Various varieties of the binary tree**
```
Full binary tree    -> 0 or 2 child node
Complete binary tree    -> draw left then draw right and min 2 child in internal nodes
Almost complete binary tree     -> complete binary tree + one child accepted
Perfect binary tree     -> complete binary tree + same level of the leaf node
Balance binary tree     -> left nodes >= right nodes
Degerate binary tree      -> single child (`ubhi patti`)
```

