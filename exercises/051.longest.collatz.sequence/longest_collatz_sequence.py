#!/usr/bin/python3
"""Exercise from Day 51/100."""
class Collatz():
    """Collatz sequencing and analysis."""
    reduction_sequence = []
    def reduce(n, count=1):
        """Reduces a given number to 1 using the Collatz method. Tracks length
        of sequence.
        
        >>> Collatz.reduce(13)[0]
        10
        """
        Collatz.reduction_sequence.append(int(n))
        count += 1
        if n % 2:
            n *= 3
            n += 1
        else:
            n /= 2
        if n == 1:
            Collatz.reduction_sequence.append(int(n))
            return count, Collatz.reduction_sequence
        return Collatz.reduce(n, count)

    def longest(limit):
        """Returns the starting number below the limit with the longest Collatz
        sequence."""
        i = 1
        longest = [0, 0] # count, starting number
        while i < limit:
            Collatz.reduction_sequence = []
            count = Collatz.reduce(i)
            if count[0] > longest[0]:
                longest = [count[0], i]
            i += 1
        return longest

    def solve():
        """Solves the exercise."""
        return Collatz.longest(1000000)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
print("Calculating solution...")
print(f"{Collatz.solve()[1]} produces the longest collatz chain among numbers below one million.")
