"""
The use of this data structre is to test membership in a set.
Compared to python's built-in set() it is more space-efficient probablistic data strucre.
In the following example, only 8 bits of memory will be used:
>>> bloom = Bloom(size=8)

Initially, the filter contains all zeros:
>>> bloom.bitstring
'00000000'

When an element is added, two bits are set to 1
since there are 2 hash functions in this implementation:
>>> "Titanic" in bloom
False
>>> bloom.add("Titanic")
>>> bloom.bitstring
'01100000'
>>> "Titanic" in bloom
True

However, sometimes only one bit is added
because both hash functions return the same value
>>> bloom.add("Avatar")
>>> "Avatar" in bloom
True
>>> bloom.format_hash("Avatar")
'00000100'
>>> bloom.bitstring
'01100100'

Not added elements should return False ...
>>> not_present_films = ("The Godfather", "Interstellar", "Parasite", "Pulp Fiction")
>>> {
...   film: bloom.format_hash(film) for film in not_present_films
... } # doctest: +NORMALIZE_WHITESPACE
{'The Godfather': '00000101',
 'Interstellar': '00000011',
 'Parasite': '00010010',
 'Pulp Fiction': '10000100'}
>>> any(film in bloom for film in not_present_films)
False

but sometimes there are false positives:
>>> "Ratatouille" in bloom
True
>>> bloom.format_hash("Ratatouille")
'01100000'

The probability increases with the number of elements added.
The probability decreases with the number of bits in the bitarray.
>>> bloom.estimated_error_rate
0.140625
>>> bloom.add("The Godfather")
>>> bloom.estimated_error_rate
0.25
>>> bloom.bitstring
'01100101'
"""
from hashlib import sha256, md5

from dataclasses import dataclass

HASH_FUNCTIONS = (sha256, md5)


@dataclass
class Bloom:
    """Bloom filter data structre"""

    bitrarray: bytes = 0b0
    size: int = 8

    def add(self, value):
        """
        Add value inside bitarray

        :type value: str | any
        :rtype: null
        """
        hs = self.hash_(value)
        self.bitrarray |= hs


    def __contains__(self, other):
        """
        Find filter value inside bitarray

        :type other: str | any
        :rtype: str
        """
        hs = self.hash_(other)
        return (hs & self.bitrarray) == hs


    def format_bin(self, bitarray):
        """
        Return bin fromat of bitarray

        :type bitarray: list[int]
        :rtype: str
        """
        res = bin(bitarray)[2:]
        return res.zfill(self.size)
    

    @property
    def bitstring(self):
        """
        Return string of the bit array.

        :rtype: str
        """
        return self.format_bin(self.bitrarray)


    def hash_(self, value):
        """
        Hash function return hash value

        :type value: str | any
        :rtype: null
        """
        res = 0b0
        for func in HASH_FUNCTIONS:
            position = (
                int.from_bytes(
                    func(value.encode()).digest(), "little"
                ) % self.size
            )
            res |= 2**position
        return res
    

    def format_hash(self, value):
        """
        Convert value into hash

        :type value: str | null
        :rtype: str
        """
        return self.format_bin(self.hash_(value))


    @property
    def estimated_error_rate(self):
        """
        First count number of 1 in bitarray then divide by bitarray size
        and power of len(HASH_FUNCTIONS)

        :rtype: float
        """
        n_ones = bin(self.bitrarray).count("1")
        return (n_ones / self.size) ** len(HASH_FUNCTIONS)
