class collatz():
    """Collatz sequencing and analysis."""
    reduction_sequence = []
    def reduce(n, count=1):
        """Reduces a given number to 1 using the Collatz method. Tracks length
        of sequence."""
        collatz.reduction_sequence.append(int(n))
        count += 1
        if n % 2:
            n *= 3
            n += 1
        else:
            n /= 2
        if n == 1:
            collatz.reduction_sequence.append(int(n))
            return count, collatz.reduction_sequence
        return collatz.reduce(n, count)

    def longest(limit):
        """Returns the starting number below the limit with the longest Collatz
        sequence."""
        i = 1
        longest = [0, 0] # count, starting number
        while i < limit:
            collatz.reduction_sequence = []
            count = collatz.reduce(i)
            if count[0] > longest[0]:
                longest = [count[0], i]
            i += 1
        return longest

    def solve():
        """Solves the exercise."""
        return collatz.longest(1000000)

print("Calculating...")
print(f"{collatz.solve()[1]} produces the longest collatz chain among numbers below one million.")
