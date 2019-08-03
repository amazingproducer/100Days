# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Let's solve it the hard way:

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

class SmallestMultiple:
    exercise_set = set(range(1,21))
    def generate_nth_prime(n):
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

    def get_from_set(a=exercise_set)):
        column_list = a
        for item in a:
            i = 2
            item_list = []
            while i:
                j = SmallestMultiple.generate_nth_prime(i)
                if item % j == 0 and item != j:
                    print("This isn't done yet.")

