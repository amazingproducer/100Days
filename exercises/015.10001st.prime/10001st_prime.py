## By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
# What is the 10001st prime number?

# I'm reluctant to reuse my n-th prime code now that I see how bad it is,
# but knowing how long it takes to reach the 10001st entry might be valuable.

class Prime:
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

print(f"Example solution (we expect 13): {Prime.generate_nth_prime(6)}")
print(f"Exercise solution: {Prime.generate_nth_prime(10001)}")
