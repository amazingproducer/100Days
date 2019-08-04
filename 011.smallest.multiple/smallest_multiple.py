# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Let's solve it the hard way:
# It would be crazy to ask our program to solve it this way. Is it cheating if
# I look for a better algorithm to do this?

# x  2  2  2  2  3  3  5  7  11 13 17 19
# ======================================
# 1  1  1  1  1  1  1  1  1  1  1  1  1
# 2  1  1  1  1  1  1  1  1  1  1  1  1
# 3  3  3  3  3  1  1  1  1  1  1  1  1
# 4  2  1  1  1  1  1  1  1  1  1  1  1
# 5  5  5  5  5  5  5  1  1  1  1  1  1
# 6  3  3  3  3  1  1  1  1  1  1  1  1
# 7  7  7  7  7  7  7  7  1  1  1  1  1
# 8  4  2  1  1  1  1  1  1  1  1  1  1
# 9  9  9  9  9  3  1  1  1  1  1  1  1
# 10 5  5  5  5  5  5  1  1  1  1  1  1
# 11 11 11 11 11 11 11 11 11 1  1  1  1
# 12 6  3  3  3  1  1  1  1  1  1  1  1
# 13 13 13 13 13 13 13 13 13 13 1  1  1
# 14 7  7  7  7  7  7  7  1  1  1  1  1
# 15 15 15 15 15 5  5  1  1  1  1  1  1
# 16 8  4  2  1  1  1  1  1  1  1  1  1
# 17 17 17 17 17 17 17 17 17 17 17 1  1
# 18 9  9  9  9  3  1  1  1  1  1  1  1
# 19 19 19 19 19 19 19 19 19 19 19 19 1
# 20 10 5  5  5  5  5  1  1  1  1  1  1

# This should give us 232792560

# For each prime number, divide each number in the sequence by the prime
# number, replacing that number in the sequence from the quotient if it is a
# whole number. If the sequence is completely unchanged, use the next prime
# number. If each item in the sequence is now 1, stop.

# ** Maintain a list of of each prime number when it is used as a divisor. The
# product of the elements of this list is the solution

class SmallestMultiple:
    exercise_set = range(2,21) # I think using this makes it not work right
    def generate_nth_prime(n): # I thought bringing this in would help
        j = [2]
        i = 3
        while len(j) < n:
            for k in j:
                if i % k == 0:
                    break
            else:
                j.append(i)
            i += 2
        return j[-1]

    def get_from_set(): # I sure wish I documented what I meant to do here when I attempted this earlier.
        i = 0
        j = None
        while not j:
            i += 1
            for item in range(20,1, -1): # Maybe because the range was backwards?
                print(item, i)
                if i % item != 0:
                    break
            else:
                return j # Oh boy does this take forever to get there
# I think doing it the long way with the tables would have been quicker than
# this way. Running it took about an hour to complete!

print(SmallestMultiple.get_from_set())
