"""Hash table with open addressing (closed hashing) with help of linear probing."""
from __future__ import annotations
from ctypes import Array

from dataclasses import dataclass


@dataclass
class DummyNode:
    """
    When delete any node in the hash table
    then we need to add dummy node else, search
    opration not working.
    """
    key: any
    value: any


@dataclass
class HashTable:
    """
    Create max-length of bucket, max-load-factor
    with m/n (size)/(max_length), size and array.
    """
    max_length: int = 8
    max_load_factor: float = 0.75
    size: int = 0
    table: Array = [None] * max_length


    def __len__(self):
        """
        Return length of the current bucket.
        
        :rtype: int
        """
        return self.size

    def _hash(self, key):
        """
        Return hash value.
        
        :type key: any
        :rtype: Any
        """
        return (hash(key) % self.max_length)

    def _increment_key(self, key):
        """
        If the collision happed then key will be
        increment at 1 position.
        
        :type key: int
        :rtype: None
        """
        return ((key + 1) % self.max_length)

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
        temp_table += self.table
        return None

    def __getitem__(self, key):
        """
        Search the key on every row of the table.
        
        :type key: any
        :rtype: any
        """
        index = self._hash(key)
        if self.table[index] is None:
            raise KeyError
        if self.table[index][0] != key:
            temp_key = index
            while self.table[index][0] != key:
                index = self._increment_key(index)
                if not index:
                    raise KeyError
                if index == temp_key:
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
        while self.table[index] is not None:
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

        
    def __delitem__(self, key):
        """
        Hash funciton travers lineary when 
        key found then add tombstone in these point
        bcz when search operation will not stop otherwise
        searching will not work.

        :type key: any
        :rtype: any
        """

        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                temp = self.table[index]
                self.table[index] = DummyNode(-1, -1)
                self.size -= 1
                return temp[1]
            index += 1
            index %= self.max_length
        return None


hstable = HashTable()
hstable["name"] = "krupesh"
print(hstable["name"])
