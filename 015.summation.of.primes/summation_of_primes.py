# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# Let's borrow some code from an earlier prime number exercise!

class PrimeToys:
    # TODO: apply optimized primal functions to this class
    # TODO: create generator: generate_next_prime(n)
    # Accepts n (the n-th prime number) as starting value
    # as input and yields a list containing all primes up to the nth.
    # calling next() on it will yield a list containing all primes
    # up to the nth+1 prime, etc
    def generate_nth_prime(n): # Borrowed from Day 7
        j = [2]
        i = 3
        while len(j) < n:
            for k in j: # because naming stuff is hard
                if i % k == 0:
                    break
            else:
                j.append(i)
            i += 2 # because incrementing by one would include even numbers. Wasteful!
        return j[-1]

    def sum_prime_ceiling(ceiling=10):
        n = 0
        i = 1
        q = 0
        while n < ceiling:
            q += PrimeToys.generate_nth_prime(i)
            i += 1
            n = PrimeToys.generate_nth_prime(i)
        return q


# Does my n-th generator work?
#print(PrimeToys.generate_nth_prime(0)) # 2 ugly
#print(PrimeToys.generate_nth_prime(1)) # 2 that's why it's ugly
#print(PrimeToys.generate_nth_prime(2)) # 3 works, but ugly

# Does my solution solve the example correctly?

#print(PrimeToys.sum_prime_ceiling()) # Seems to work; prints 17

print(PrimeToys.sum_prime_ceiling(2000000))
