#!/usr/bin/env python3
"""
Initialize trie  data structre.
A Trie/Prefix Tree is a kind of search tree used to provide quick lookup
of words/patterns in a set of words.

Example:

             root
             / \
            a   b
             \    \
             p    a
            / \   /
           p   d n

>>> words = ["apple", "bannana"]
>>> trie = Trie()
>>> trie.insert_many(words)
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import DefaultDict


@dataclass(repr=False)
class Trie:
    """
    Initialize node which has store word, next nodes with dictionary format.
    """
    node= dict()
    is_leaf: bool = False

    @staticmethod
    def __type(word: str) -> None:
        """
        Check type of the word
        If word is not string return false, else true        
        """
        if isinstance(word, str):
            return True
        return False

    def insert_many(self, words: list[str]) -> None:
        """
        Insert a list of words into the trie.

        >>> words = ["apple", "bannana"]
        >>> trie = Trie()
        >>> trie.insert_many(words)
        None
        """
        for word in words:
            self.insert(word)
        return None

    def insert(self, word: str) -> None:
        """
        Insert single word into the trie

        >>> word = "apple"
        >>> trie = Trie()
        >>> trie.insert(word)
        None
        >>> print(trie.repr())
        >>> trie.insert(5)
        Traceback (most recent call last):
            ...
        TypeError: Please insert valid word
        """
        assert self.__type and word, "Please insert valid word"

        curr = self
        for itr in word:
            if itr not in curr.node:
                curr.node[itr] = Trie()
            curr = curr.node[itr]
        curr.is_leaf = True
        return None

    def search(self, word: str) -> bool:
        """
        Search single word into the trie
        If the word is present it will return true, else false

        >>> word = "apple"
        >>> trie = Trie()
        >>> trie.search(word)
        True | False
        >>> trie.search(6)
        Traceback (most recent call last):
            ...
        TypeError: Please insert valid word
        """
        assert self.__type and word, "Please insert valid word"

        curr = self
        for itr in word:
            if itr not in curr.node:
                return False
            curr = curr.node[itr]
        return curr.is_leaf
    
    @staticmethod
    def __del(curr: Trie, word: str, index: int=0) -> bool:
        if index == len(word):

            # If word does not exist
            if not curr.is_leaf:
                return False
            curr.is_leaf = False
            return len(curr.node) == 0

        char = word[index]
        char_node = curr.nodes.get(char)

        # If char not exist in the current index of the trie
        # for example, index = 1, word = "apple", word[index] = a
        # a should be exist in the current index, if not return false
        if not char_node:
            return False

        delete_curr = Trie.__del(char_node, word, index+1)
        if delete_curr:
            del curr.node[char]
            return len(curr.node) == 0
        return delete_curr

    def delete(self, word: str) -> None:
        """
        Deletation single word into the trie
        If word exist in the trie return true after deletation, else false

        >>> word = "apple"
        >>> trie = Trie()
        >>> trie.delete(word)
        True | False
        >>> trie.delete(456)
        Traceback (most recent call last):
            ...
        TypeError: Please insert valid word
        """
        assert self.__type and word, "Please insert valid word"

        return self.__del(self, word)

words = "apple bannna".split()
trie = Trie()
trie.insert_many(words)
