# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

class PrimeToys:
    # Borrowed from day 19
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

    def get_nth_prime(n):
        j = [2]
        i = 3
        while len(j) < n:
            if PrimeToys.is_prime(i):
                j.append(i)
            i += 2
        return j, j[-1]

    def generate():
        j = [2]
        i = 3
        while i:
            if PrimeToys.is_prime(i):
                j.append(i)
                yield [j, j[-1]]
            i += 2

    def get_sum(ceiling=10):
        p = PrimeToys.generate()
        n = 0
        r = 0
        while n < ceiling:
            q = next(p)
            if q[-1] < ceiling:
                n = q[-1]
                r = sum(q[0])
            else:
                return r


print(f"Testing example (expecting 17): {PrimeToys.get_sum()}")
import datetime
start_time = datetime.datetime.utcnow()
print(f"Solution start time: {start_time}")
print(f"Attempting solution: {PrimeToys.get_sum(2000000)}")
finish_time = datetime.datetime.utcnow()
print(f"Finish time: {finish_time}")
print(f"Elapsed time: {finish_time - start_time}")
