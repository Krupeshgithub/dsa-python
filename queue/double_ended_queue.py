"""Implementation of double ended queue"""
from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Iterable
from typing import Any


class Deque:
    """
    Deque data structure.
    Operations
    ----------
    append(val: Any) -> None
    appendleft(val: Any) -> None
    extend(iterable: Iterable) -> None
    extendleft(iterable: Iterable) -> None
    pop() -> Any
    popleft() -> Any
    Observers
    ---------
    is_empty() -> bool
    Attributes
    ----------
    _front: _Node
        front of the Deque a.k.a. the first element
    _back: _Node
        back of the element a.k.a. the last element
    _len: int
        the number of nodes
    """
    __slot__ = ('_front', '_back', '_len')

    @dataclass
    class _Node:
        """
        Representation of the node.
        Contains a value and a pointer to the next and prev node.
        """
        val: Any = None
        next: Deque._Node | None = None
        prev: Deque._Node | None = None


    def __init__(
        self,
        iterable: Iterable[Any] | None = None
    ) -> None:
        self._front: Any = None
        self._back: Any = None
        self._len: int = 0

        if iterable is not None:
            # Append val in self.
            for itr in iterable:
                self.append(itr)


    def append(self, val: Any) -> None:
        """
        Adds val to the end of the Deque.
        Time complexity: O(1)
        >>> our_Deque_1 = Deque([1, 2, 3])
        >>> our_Deque_1.append(4)
        >>> our_Deque_1
        [1, 2, 3, 4]
        >>> our_Deque_2 = Deque('ab')
        >>> our_Deque_2.append('c')
        >>> our_Deque_2
        ['a', 'b', 'c']
        >>> from collections import Deque
        >>> Deque_collections_1 = Deque([1, 2, 3])
        >>> Deque_collections_1.append(4)
        >>> Deque_collections_1
        Deque([1, 2, 3, 4])
        >>> Deque_collections_2 = Deque('ab')
        >>> Deque_collections_2.append('c')
        >>> Deque_collections_2
        Deque(['a', 'b', 'c'])
        >>> list(our_Deque_1) == list(Deque_collections_1)
        True
        >>> list(our_Deque_2) == list(Deque_collections_2)
        True
        """
        node = self._Node(val, None, None)
        if self.is_empty():
            # _front = _back
            self._front = self._back = node
            self._len = 1
        else:
            self._back.next = node
            node.prev = self._back
            self._back = node   # Change position of back

            self._len += 1

        # Make sure there were no error
        assert not self.is_empty(), "Error on appending node"


    def appendleft(self, val: Any) -> None:
        """
        Adds val to the end of the Deque.
        Time complexity: O(1)
        >>> our_Deque_1 = Deque([1, 2, 3])
        >>> our_Deque_1.appendleft(4)
        >>> our_Deque_1
        [4, 1, 2, 3]
        >>> our_Deque_2 = Deque('ab')
        >>> our_Deque_2.appendleft('c')
        >>> our_Deque_2
        ['c', 'a', 'b']
        >>> from collections import Deque
        >>> Deque_collections_1 = Deque([1, 2, 3])
        >>> Deque_collections_1.appendleft(4)
        >>> Deque_collections_1
        Deque([4, 1, 2, 3])
        >>> Deque_collections_2 = Deque('ab')
        >>> Deque_collections_2.appendleft('c')
        >>> Deque_collections_2
        Deque(['c', 'a', 'b'])
        >>> list(our_Deque_1) == list(Deque_collections_1)
        True
        >>> list(our_Deque_2) == list(Deque_collections_2)
        True
        """
        node = self._Node(val, None, None)
        if self.is_empty():
            # _front = _back
            self._front = self._back = node
            self._len = 1
        else:
            self._front.prev = node
            node.next = self._front
            self._front = node  # Change position of the front node

            self._len += 1
        
        # If there any error occured.
        assert not self.is_empty(), "Error on appendleft node"


    def extend(self, lst: list) -> None:
        """
        Appends every value of iterable to the end of the Deque.
        Time complexity: O(n)
        >>> our_Deque_1 = Deque([1, 2, 3])
        >>> our_Deque_1.extend([4, 5])
        >>> our_Deque_1
        [1, 2, 3, 4, 5]
        >>> our_Deque_2 = Deque('ab')
        >>> our_Deque_2.extend('cd')
        >>> our_Deque_2
        ['a', 'b', 'c', 'd']
        >>> from collections import Deque
        >>> Deque_collections_1 = Deque([1, 2, 3])
        >>> Deque_collections_1.extend([4, 5])
        >>> Deque_collections_1
        Deque([1, 2, 3, 4, 5])
        >>> Deque_collections_2 = Deque('ab')
        >>> Deque_collections_2.extend('cd')
        >>> Deque_collections_2
        Deque(['a', 'b', 'c', 'd'])
        >>> list(our_Deque_1) == list(Deque_collections_1)
        True
        >>> list(our_Deque_2) == list(Deque_collections_2)
        True
        """
        for itr in lst:
            self.append(itr)


    def extendleft(self, lst: list) -> None:
        """
        Appends every value of iterable to the end of the Deque.
        Time complexity: O(n)
        >>> our_Deque_1 = Deque([1, 2, 3])
        >>> our_Deque_1.extendleft([4, 5])
        >>> our_Deque_1
        [4, 5, 1, 2, 3]
        >>> our_Deque_2 = Deque('ab')
        >>> our_Deque_2.extendleft('cd')
        >>> our_Deque_2
        ['c', 'd', 'a', 'b']
        >>> from collections import Deque
        >>> Deque_collections_1 = Deque([1, 2, 3])
        >>> Deque_collections_1.extendleft([4, 5])
        >>> Deque_collections_1
        Deque([1, 2, 3, 4, 5])
        >>> Deque_collections_2 = Deque('ab')
        >>> Deque_collections_2.extendleft('cd')
        >>> Deque_collections_2
        Deque(['c', 'd', 'a', 'b'])
        >>> list(our_Deque_1) == list(Deque_collections_1)
        True
        >>> list(our_Deque_2) == list(Deque_collections_2)
        True
        """
        for itr in lst:
            self.appendleft(itr)


    def pop(self) -> Any:
        """
        Removes the last element of the Deque and returns it.
        Time complexity: O(1)
        @returns topop.val: the value of the node to pop.
        >>> our_Deque = Deque([1, 2, 3, 15182])
        >>> our_popped = our_Deque.pop()
        >>> our_popped
        15182
        >>> our_Deque
        [1, 2, 3]
        >>> from collections import Deque
        >>> Deque_collections = Deque([1, 2, 3, 15182])
        >>> collections_popped = Deque_collections.pop()
        >>> collections_popped
        15182
        >>> Deque_collections
        Deque([1, 2, 3])
        >>> list(our_Deque) == list(Deque_collections)
        True
        >>> our_popped == collections_popped
        True
        """
        # Make sure Dequeu has element for pop
        assert not self.is_empty(), "Deque has empty"

        if self._front == self._back:
            temp = self._front
            self._front = self._back = None
        else:
            temp = self._back
            self._back = self._back.prev
            self._back.next = self._back.next.prev = None

        self._len -= 1

        return temp.val


    def popleft(self) -> Any:
        """
        Removes the last element of the Deque and returns it.
        Time complexity: O(1)
        @returns topop.val: the value of the node to pop.
        >>> our_Deque = Deque([1, 2, 3, 15182])
        >>> our_popped = our_Deque.popleft()
        >>> our_popped
        1
        >>> our_Deque
        [2, 3, 15182]
        >>> from collections import Deque
        >>> Deque_collections = Deque([1, 2, 3, 15182])
        >>> collections_popped = Deque_collections.pop()
        >>> collections_popped
        15182
        >>> Deque_collections
        Deque([1, 2, 3])
        >>> list(our_Deque) == list(Deque_collections)
        True
        >>> our_popped == collections_popped
        True
        """
        # Make sure Dequeu has element for pop
        assert not self.is_empty(), "Deque has empty"

        if self._front == self._back:
            temp = self._front
            self._front = self._back = None
        else:
            temp = self._front
            self._front = self._front.next
            self._front.prev = self._front.prev.next = None

        self._len -= 1

        return temp.val


    def is_empty(self) -> bool:
        """
        Checks if the deque is empty.
        Time complexity: O(1)
        >>> our_deque = Deque([1, 2, 3])
        >>> our_deque.is_empty()
        False
        >>> our_empty_deque = Deque()
        >>> our_empty_deque.is_empty()
        True
        >>> from collections import deque
        >>> empty_deque_collections = deque()
        >>> list(our_empty_deque) == list(empty_deque_collections)
        True
        """
        return self._len == 0
    

    def __len__(self) -> int:
        """
        Implements len() function. Returns the length of the deque.
        Time complexity: O(1)
        >>> our_deque = Deque([1, 2, 3])
        >>> len(our_deque)
        3
        >>> our_empty_deque = Deque()
        >>> len(our_empty_deque)
        0
        >>> from collections import deque
        >>> deque_collections = deque([1, 2, 3])
        >>> len(deque_collections)
        3
        >>> empty_deque_collections = deque()
        >>> len(empty_deque_collections)
        0
        >>> len(our_empty_deque) == len(empty_deque_collections)
        True
        """
        return self._len
    

    def __eq__(self, other: object) -> Any:
        """
        Implements "==" operator. Returns if *self* is equal to *other*.
        Time complexity: O(n)
        >>> our_deque_1 = Deque([1, 2, 3])
        >>> our_deque_2 = Deque([1, 2, 3])
        >>> our_deque_1 == our_deque_2
        True
        >>> our_deque_3 = Deque([1, 2])
        >>> our_deque_1 == our_deque_3
        False
        >>> from collections import deque
        >>> deque_collections_1 = deque([1, 2, 3])
        >>> deque_collections_2 = deque([1, 2, 3])
        >>> deque_collections_1 == deque_collections_2
        True
        >>> deque_collections_3 = deque([1, 2])
        >>> deque_collections_1 == deque_collections_3
        False
        >>> (our_deque_1 == our_deque_2) == (deque_collections_1 == deque_collections_2)
        True
        >>> (our_deque_1 == our_deque_3) == (deque_collections_1 == deque_collections_3)
        True
        """

        if not isinstance(other, Deque):
            return NotImplemented
        
        curr = self._front
        oth = other._front

        if len(curr) != len(oth):
            return False

        while curr and oth:
            if curr.val != oth.val:
                return False
            curr = curr.next
            oth = oth.next
        else:
            return True


    def __repr__(self) -> str:
        """
        Implements representation of the deque.
        Represents it as a list, with its values between '[' and ']'.
        Time complexity: O(n)
        >>> our_deque = Deque([1, 2, 3])
        >>> our_deque
        [1, 2, 3]
        """
        lst = list()
        temp = self._front
        while temp:
            lst.append(temp.val)
            temp = temp.next
        
        return f"[{', '.join(repr(itr) for itr in lst)}]"


    def clear(self) -> None:
        """
        Time complexity: O(1)
        >>> deque = Deque([1, 2, 3])
        >>> deque.clear()
        0
        >>> deque
        None
        """
        self._front = self._rear = None
