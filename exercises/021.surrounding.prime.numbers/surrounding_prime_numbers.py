#Given a positive integer n, determine the greatest prime number which is less than n. Determine the lowest prime number which is greater than n.

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

def get_nearest_primes(n):
    if n < 3:
        return ValueError("Integer must be greater than 3")
    p = generate_prime()
    q = []
    l = 0
    g = 0
    while g <= n:
        q = next(p)
        g = q[-1]
        if q[-1] == n:
            l = q[0][-2]
            q = next(p)
            g = q[-1]
        elif q[-1] > n:
            l = q[0][-3]
    return l, g

def prime_string(x:bool):
    if x == True:
        return " (prime) "
    return " "

for i in range(-3,101):
    x = is_prime(i)
    print(f"The prime numbers surrounding {i}{prime_string(x)}are: {get_nearest_primes(i)}")
