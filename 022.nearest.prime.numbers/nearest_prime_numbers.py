# Given positive integers n and y, return the y prime number(s) with the least
# difference in value from n.

# How do I handle the case of more than y equidistant primes?

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**.5) + 1, 2):
            if n % i == 0:
                return False
        return True

def generate_prime():
    j = [2]
    i = 3
    while i:
        if is_prime(i):
            j.append(i)
            yield [j, j[-1]]
        i += 2

# Okay, building off of yesterday's work, let's see if we can't use what we
# learned about using generators to do something a little more complex.

# We need to build a list of tuples containing a prime number and its distance
# from n.

# When a value from this list meets or exceeds n, let's be lazy and call the
# generator to add y more list entries.

# Once this most-likely bloated list has been generated, we can then iterate
# over the list, evaluating the "distance" values in each tuple to determine
# the bottom y values (excluding 0) and report their primes.

def get_nearest_primes(n, y=2):
    if n < 1:
        # Integer must be positive - using 1 instead
        n = 1
    p = generate_prime()
    r = []
    s = y + 1
    g = 0
    c = y
    z = []
    while s > 0:
        q = next(p)
        r.append((q[-1], abs(q[-1] - n)))
        if q[-1] > n:
            q = next(p)
            r.append((q[-1], abs(q[-1] - n)))
            s -= 1
    for i in range(len(r) - 1):
        if r[i][1] == 0:
            r.pop(i)
    for prime, distance in sorted(r, key=lambda x: x[1]):
        if c > 0:
            z.append(prime)
            c -= 1
    return z

for i in range(10,101):
    print("Nearest", str(i), "primes to 101:", sorted(get_nearest_primes(101,i)))

