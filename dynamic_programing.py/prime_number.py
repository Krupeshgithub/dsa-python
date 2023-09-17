"""Module to operations with prime numbers"""
import math


def is_prime(number):
    """
    Checks to see if a number is a prime in O(sqrt(n))
    A number is prime if it has exactly two factors: 1 and it self.

    :type number: int
    :rtype: bool
    """
    # Precodition
    assert isinstance(number, int) and (
        number>=0
    ), "`number` must beeen an int and positive"

    if 1 < number < 4:
        # 2 and 3 are primes
        return True
    elif number < 2 or not number % 2:
        # Negatives 0, 1 and all even numbers are not prime
        return False

    return not any(
        not number % itr for itr in range(
            3, int(math.sqrt(number), 2)
        )
    )

print(is_prime(951))
