from itertools import takewhile, count
from math import sqrt


def is_prime(n):
    def compute_bi(a, m):
        b = pow(a, m, n)
        if b == 1 or b == (n - 1):
            return True

        old_b = set()
        while True:
            b = pow(b, 2, n)
            if (b == 1) or (b in old_b):
                return False
            if (b == (n - 1)):
                return True
            old_b.add(b)
    if (n == 2) or (n == 1):
        return True
    if (n % 2) == 0:
        return False

    k = list(takewhile(lambda x: ((n - 1) % (2 ** x)) == 0, count()))[-1]
    m = (n - 1) / (2 ** k)

    return all(compute_bi(x, m) for x in [2,3,5])


#print list(enumerate(map(is_prime, xrange(1, 101)), start=1))
n = 600851475143
for x in range(775147, 1, -2):
    if (n % x) == 0 and is_prime(x):
            print x
            break
