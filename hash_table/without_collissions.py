"""Custom hash table. Without solving collisions."""

from typing import Any


class HashTable:

    def __init__(self, length=4):
        """
        :intro: initialize array with empty values.
        :length type: int
        :rtype: Array
        """
        self.array = [None] * length
    
    def hash_(self, key):
        """
        :intro: Get the index of our array for a specific string key.
        :key type: int
        :rtype: floot 
        """
        length = len(self.array)
        return hash(key) % length
    
    def __setitem__(self, key, value):
        """
        :intro: Add a value to our array by its key.
        :key type: Any
        :value type: Any
        :rtype: None
        """
        index = self.hash_(key)
        if self.array[index] is not None:
            for itr in self.array[index]:
                if itr[0] == key:
                    itr[1] = value
                    break
            # If not breaks was hit in the for loop, 
            # it means that no existing key was found.
            else:
                self.array[index].append[[key,value]]
        else:
            self.array[index] = list()
            self.array[index].append([key, value])

    def __getitem__(self, key):
        """
        :intro: Get a value by a key.
        :key type: int
        :rype: Any
        """
        index = self.hash_(key)
        if self.array[index] is None:
            return KeyError()
        else:
            for itr in self.array[index]:
                if itr[0] == key:
                    return itr[1]
            return KeyError()

hstable = HashTable()
hstable[1] = 'krupesh'
print(hstable.__dict__)
