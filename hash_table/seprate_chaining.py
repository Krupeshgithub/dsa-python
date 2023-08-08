"""Custom hash table. With collision separate chaining process."""

class ListNode:
    def __init__(self, key, value):
        """
        :intro: Each node represent key and value pair,
                as well as a pointer of the next node.
        :key type: Any
        :value type: Any
        :rtype: Optional[List[key, value, next]]
        """
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, length=100):
        """
        :intro: decorator will contain the array of the 
                [key, value] pairt if there are any collision
                found then  store the data with help of ListNode.
        :length type: int
        :rtype: None
        """
        self.length = length
        self.size = 0
        self.table = [None] * length
    
    def _hash(self, key):
        """
        :intro: This method takes a key and returns an index 
                in the array where the key-value pair should be 
                stored. We will use Python's built-in hash function
                to hash the key and then use the modulo operator
                to get an index in the array.
        :key type: Any
        :rtype: floor
        """
        return hash(key) % self.length

    def __setitem__(self, key, value):
        """
        :intro: This method takes key and value pair, if
                the key has been repeted then will store
                the value with node it's called chaining process.
        :key type: Any
        :value type: Any
        :rtype: None
        """
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = ListNode(key, value)
            self.size += 1
        else:
            curr = self.table[index]
            while curr:
                if curr.key == key:
                    curr.value = value
                    return None
                curr = curr.next
            new_node = ListNode(key, value)
            curr.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def __getitem__(self, key):
        """
        :intro: This method takes key and return the values 
                of that contain key. If collision found then
                solved chain list and then return the value.
        :key type: Any
        :rtype: Any
        """
        index = self._hash(key)

        curr = self.table[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        else:
            return KeyError()

    def __delitem__(self, key):
        """
        :intro: This method delete all values which contain
                key.
        :key type: Any
        :rtype: Any
        """
        index = self._hash(key)

        curr = self.table[index]
        prev = None
        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.table[index] = curr.next
                return None
            self.size -= 1
            curr = curr.next
            prev = curr
        else:
            raise KeyError()

    def __str__(self):
        """
        :intro: This method return string of the all data
                which store in the system.
        :rtype: List
        """
        lst = list()
        for itr in range(self.length):
            curr = self.table[itr]
            while curr:
                lst.append((curr.key, curr.value))
                curr = curr.next
        return str(lst)
    
hstable = HashTable()
hstable["name"] = "krupesh"
hstable["last_name"] = "patel"
hstable["last_name"] = "varma"
print(hstable.__str__())
