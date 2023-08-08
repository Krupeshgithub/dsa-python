**Hash function**

- It is the process of converting a given key into another value, with the help of a hash function. A hash function is nothing but a mathematical algorithm which helps generate a new value for a given input. The result of a hash function is called a hash, or a hash value.

**Hash table**

- A hash table is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found.

**Collision**

- Two or more keys can generate same hash values sometimes. This is called a collision. A collision can be handled using various techniques.

***Separate Chaining Technique***


- The idea is to make each cell of the hash table point to a linked list of records that have the same hash function values. It is simple but requires additional memory outside the table. In this technique, the worst case occurs when all the values are in the same index or linked list, making the search complexity linear (n=length of the linked list). 

> - Note: This method should be used when we do not know how many keys will be there or how frequently the insert/delete operations will take place.


***Open Addressing***

- Open addressing is a collision handling technique used in hashing where, when a collision occurs (i.e., when two or more keys map to the same slot), the algorithm looks for another empty slot in the hash table to store the collided key.
