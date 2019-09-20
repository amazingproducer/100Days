#!/bin/usr/python3
"""Exercise from Day 4/100."""


# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


class FancyConditionalSum:
    """
    Test against the example result.

    >>> FancyConditionalSum.example()
    23
    """
    def example():
        """Ensures that the algorithm produces the example result."""
        sum = 0
        for i in range(1, 10):
            if i % 5 == 0:
                sum += i
            elif i % 3 == 0:
                sum += i
        return sum

    def solve():
        """Use the algorithm to solve the exercise."""
        sum = 0
        for i in range(1, 1000):
            if i % 5 == 0:
                sum += i
            elif i % 3 == 0:
                sum += i
        return sum

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
print(FancyConditionalSum.solve())
