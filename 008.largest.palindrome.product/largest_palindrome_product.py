# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# How do I check for a palindrome? Abuse the text reverse feature?
# How do i efficiently multiply all the things?

def lpd():
    for factor1 in reversed(range(100, 1000)):
        for factor2 in reversed(range(100, 1000)):
            if str(factor2 * factor1) == str(factor2 * factor1)[::-1]:
                return((factor2 * factor1), factor1, factor2)
            factor2 += 1
        factor1 += 1

