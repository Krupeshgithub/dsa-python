"""Hash table with open addressing with help of linear probing."""

class HashTable:
    def __init__(self):
        """
        :intro: Table, table length and load factor define on
                this decorator.
        :rtype: None
        """
        self.max_length = 8
        self.max_load_factor = 0.75
        self.size = 0
        self.table = [None] * self.max_length
    
    def __len__(self):
        """
        :intro: Return length of the current table.
        :rtype: int
        """
        return self.size

    def _hash(self, key):
        """
        :intro: Return hash value.
        :key type: Any
        :rtype: Any
        """
        return (hash(key) % self.max_length)

    def _increment_key(self, key):
        """
        :intro: If the collision happed then key will be
                increment at 1 position.
        :key type: int
        :rtype: None
        """
        return ((key + 1) % self.max_length)

    def _resize(self):
        """
        :intro: If the hash table length is full then
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
        :intro: Search the key on every row of the table.
        :key type: Any
        :rtype: Any
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
        :intro: Set key and value on the index of
                hash table.
        :key type: Any
        :value type: Any
        :rtype: Any
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

hstable = HashTable()
hstable["name"] = "krupesh"
print(hstable["name"])
