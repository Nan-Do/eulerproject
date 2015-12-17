from itertools import combinations
import sys


def get_primes(n):
    def temp(values):
        upperBoundSquareRoot = int(n ** 0.5)
        primes = set()
        isComposite = [False for _ in xrange(n)]
        for v in values:
            if v > upperBoundSquareRoot:
                break
            if not isComposite[v]:
                primes.add(v)
                for k in xrange(v*v, n, v):
                    isComposite[k] = True
        for m in xrange(upperBoundSquareRoot, n):
            if not isComposite[m]:
                primes.add(m)
        return primes

    values = [2, 3]
    for x in xrange(6, n, 6):
        values.append(x-1)
        values.append(x+1)

    return temp(values)

def gen_is_prime(size):
    primes_buffer = get_primes(size)
    def _(n):
        if n in primes_buffer:
            return True
        if (n % 2) == 0:
            return False
        for x in xrange(3, int(n**0.5), 2):
            if (n % x) == 0:
                return False
        return True
    return _
is_prime = gen_is_prime(120000)

def check_combinations(combination):
    for c in combinations(combination, 2):
        a = str(c[0]) + str(c[1])
        b = str(c[1]) + str(c[0])
        if not is_prime(int(a)) or not is_prime(int(b)):
            return False
    return True


def gen_combinations(numbers, length=3):
    for c in combinations(numbers, length):
        yield c

primes = get_primes(10000)
for c in gen_combinations(primes,4):
    if check_combinations(c):
        print c
