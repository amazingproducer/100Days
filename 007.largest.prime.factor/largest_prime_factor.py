# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Ugh. Prime numbers. How do I even start? Let's consider what makes a natural
# number prime: its factors. Prime numbers have only two factors: 1 and the
# number itself. What's an efficient way of determining a number is prime?

# Do I use the silly rules I learned in grade school? Like:
#   "A number is not prime if it is even."
#   "A number is not prime if it ends in 5."
#   "A number is not prime if its digits are divisible by 3"
#   "Aside from 2 and 5, a prime number must end in 1, 3, 7, or 9"

# How do I efficiently determine a number's factors?
# Should such a general approach be used to solve this specific problem?

# Should I first build a set of primes and check each of the nearest primes to
# the target number are factors of the target number? Or should I start from
# the furthest ones?

# If our earlier rules can be trusted, it's possible that our target number is
# prime, perhaps we should start by checking for this possibility.

class NaivePrimeChecking:
# TODO: This needs to be remade
    def is_prime(n):
        if NaivePrimeChecking.factor_2(n) == False and NaivePrimeChecking.factor_3(n) == False and NaivePrimeChecking.factor_5(n) == False:
            return True
        return False

# TODO: Optimize this and maybe change its output to yield
    def generate_nth_prime(n):
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

# Let's try to make this faster using rules we learned
# After 2, primes are odd numbers
# The largest prime factor will be no more than sqrt(n)

    def get_prime_factor(n=600851475143):
        r = n # i think i can do this with just n now
        factors = []
        # manage the case of even numbers
        # manage the special case where r is 2
        while r % 2 == 0:
            factors.append(2)
            r /= 2
        # manage the case where r is prime, which should be odd
        # we can use the fancy range parameter to ensure this
        # instead of i += 2
        for i in range(3, int(r**.5) + 1, 2):
            while r % i == 0:
                factors.append(int(r))
                r /= i
        # manage the case of a prime number as n
        if r > 2:
            factors.append(int(r))
        return factors

print("Testing for prime input (should output [13]): ", NaivePrimeChecking.get_prime_factor(13))
print("Solution: ", NaivePrimeChecking.get_prime_factor()[-1])
