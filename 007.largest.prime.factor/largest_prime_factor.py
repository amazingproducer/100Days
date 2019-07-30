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
    def factor_2(n):
        if n % 2 == 0:
            return True
        return False

    def factor_3(n):
        i = 0
        while n:
            i, n = i + n % 10, n // 10
        if i % 3 == 0:
            return True
        return False

    def factor_5(n):
        if n % 10 == 5:
            return True
        return False

    def end_check(n):
        if n % 10 in (1, 3, 7, 9):
            return True
        return False

    def is_prime(n):
        if NaivePrimeChecking.factor_2(n) == False and NaivePrimeChecking.factor_3(n) == False and NaivePrimeChecking.factor_5(n) == False:
            return True
        return False

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

    def get_prime_factor(n):
        r = n
        d = 2
        factors = []
        while r > 1:
            while r % d == 0:
                factors.append(d)
                r /= d
            d += 1
        return factors[-1]





print(NaivePrimeChecking.get_prime_factor(600851475143))
#print(NaivePrimeChecking.generate_nth_prime(6))
#print(NaivePrimeChecking.factor_3(3366339))
#print(NaivePrimeChecking.end_check(600851475143))

