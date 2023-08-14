"""Hash table open addressing with help of quadratic probing."""

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

    def _increment_key(self, index):
        """
        :intro: If the collision happed then key will be
                increment at 1 position.
        :key type: int
        :rtype: None
        """
        count = 1
        while self.table[index] == 1:
            index = (index + (count * count)) % self.max_length
            count += 1
        return ((index + 1) % self.max_length)

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
        for key in temp_table:
            if key:
                self.table[key[0]] = key[1]
        
        return None
    
    def __getitem__(self, key):
        """
        :intro: Search the key on every row of the table.
        :key type: Any
        :rtype: Any
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
        :intro: Set key and value on the index of
                hash table.
        :key type: Any
        :value type: Any
        :rtype: Any
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
