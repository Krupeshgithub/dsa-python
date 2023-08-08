**Doubly Linked List**

- First, let’s discuss what an array is. An array, is a collection of elements of the same data type that are present in adjacent memory locations. We can also say that elements in an array are contiguous.

- A list a collection of elements of different data types that are not contiguous.

> **_NOTE:_**  The elements can be in different memory locations, but the references for these elements are stored in contiguous memory locations.

**What is linked list?**

- A linked list is a collection of nodes. Since linked lists can be noncontiguous, we use nodes to store the value of elements and create links between them so that they are in sequential order. Each node consists of pointers that link to the next node/next element in the list.

- In singly-linked lists, we only use the next pointer in each node, but in doubly linked lists we also add a previous pointer that links each element to its previous element. This helps us to traverse in both directions.