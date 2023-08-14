""" Hash table (open addressing) with linear probing. """

class HashTable:
    def __init__(self):
        """
        :intro: Create array which store keys.
        :rtype: None
        """
        self.max_length = 8
        self.max_load_factor = 0.75
        self.size = 0
        self.table = [None] * self.max_length

    def __len__(self):
        """
        :intro: Return length of the current table.
        :rtype: None
        """
        return self.size
    
    def _hash(self, key):
        """
        :intro: Return hash value.
        :key type: Any
        :rtype: Any
        """
        return (hash(key) % self.max_length)
    
    def _increment_key(self, index):
        """
        :intro: If the collision happend then key will be
                increment at 1 position.
        :key type: int
        :rtype: None
        """
        return ((index + 1) % self.max_length)
    
    def _resize(self):
        """
        :intro: If the length of the table is full then
                increase the table length twise to the current
                size.
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
        :intro: Search the key on table.
        :key type: Any
        :rtype: Any
        """
        index = self._hash(key)
        if not self.table[index]:
            raise KeyError
        if self.table[index][0] == key:
            return index
        else:
            temp_key = index
            while self.table[index][0] != key:
                index = self._increment_key(index)
                if not index:
                    raise KeyError
                if index == temp_key:
                    raise KeyError
        return self.table[index][0]

    def __setitem__(self, key, value):
        """
        :intro: Set tuple(key, value) pair with
                hash table.
        :key type: Any
        :value type: Any
        :rtype: None
        """
        self.size += 1
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.size -= 1
                self.table[index][1] = value
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