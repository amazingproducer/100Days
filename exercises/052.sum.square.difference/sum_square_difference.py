#!/usr/bin/python3
"""Exercise from day 52/100."""
class SumSquare():
    """
    Calculate the difference between the sum of the squares of the first n
    natural numbersand the square of the sum of the first n natural numbers.

    >>> SumSquare.solve(10)
    2640
    """
    def sum(x, y):
        return x + y

    def square(n):
        return n * n

    def diff(x, y):
        return abs(x-y)

    def solve(n=100):
        sum_of_squares = 0
        square_of_sums = 0
        sums = 0
        squares = []
        for i in range(n+1):
            sums = SumSquare.sum(sums, i)
            squares.append(SumSquare.square(i))
        for i in squares:
            sum_of_squares = SumSquare.sum(sum_of_squares, i)
        square_of_sums = SumSquare.square(sums)
        return SumSquare.diff(sum_of_squares, square_of_sums)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

print(f"Solution: {SumSquare.solve()}")
