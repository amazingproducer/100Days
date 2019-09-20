#!/usr/bin/python3
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.
What is the 10001st prime number?
"""

class Prime:
    def generate_nth_prime(n):
        """Return the n-th prime number when given an integer n.

        >>> Prime.generate_nth_prime(6)
        13
        """
        j = [2]
        i = 3
        while len(j) < n:
            for k in j:  # because naming stuff is hard
                if i % k == 0:
                    break
            else:
                j.append(i)
            i += 2  # because incrementing by one would include even numbers. Wasteful!
        return j[-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod(report=True, exclude_empty=True)

print(f"Exercise solution: {Prime.generate_nth_prime(10001)}")
