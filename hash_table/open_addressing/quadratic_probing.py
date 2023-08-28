"""Hash table open addressing with help of quadratic probing."""
from __future__ import annotations
from ctypes import Array

from dataclasses import dataclass


@dataclass
class HashTable:
    """
    Table, table length and load factor define on
    this instace variables.
    """
    max_length: int = 8
    max_load_factor: float = 0.75
    size: int = 0
    table: Array = [None] * max_length


    def __len__(self):
        """
        Return length of the current table.

        :rtype: int
        """
        return self.size

    def _hash(self, key):
        """
        Return hash value.

        :type key: any
        :rtype: any
        """
        return (hash(key) % self.max_length)

    def _increment_key(self, index):
        """
        If the collision happed then key will be
        increment at 1 position.

        :type key: int
        :rtype: None
        """
        count = 1
        while self.table[index] is None:
            index = (index + (count * count)) % self.max_length
            count += 1
        return ((index + 1) % self.max_length)

    def _resize(self):
        """
        If the hash table length is full then
        increase the table length with twise size.

        :rtype: None
        """
        self.max_length *= 2
        self.size = 0
        temp_table = self.table
        self.table = [None] * self.max_length
        for key in temp_table:
            if key:
                self.table[key[0]] = key[1]
        
        return None
    
    def __getitem__(self, key):
        """
        Search the key on every row of the table.

        :type key: any
        :rtype: any
        """
        index = self._hash(key)
        if not self.table[index]:
            raise KeyError
        if self.table[index] != key:
            temp_key = index
            while self.table[index[0]] != key:
                index = self._increment_key(index)
                if not index\
                    or temp_key == index:
                    raise KeyError
        return index

    def __setitem__(self, key, value):
        """
        Set key and value on the index of
        hash table.

        :type key: any
        :type value: any
        :rtype: any
        """
        self.size += 1
        index = self._hash(key)
        while self.table[index]:
            if self.table[index][0] == key:
                self.size -= 1
                break
            index = self._increment_key(index)
        _tuple = (key, value)
        self.table[index] = _tuple
        if (
            self.size / float(self.max_length)
        ):
            self._resize()

hstable = HashTable()
hstable[11804562] = "Dhanush"
print(hstable[11804562])

hstable[11804573] = "Krupesh"
print(hstable[11804573])

hstable[11804584] = "Omeswar"
print(len(hstable))
print(hstable[11804584])


"""
Reference:
    "https://www.scaler.com/topics/quadratic-probing/"
"""
