from itertools import combinations, takewhile, cycle, count
from operator import pos, neg, mul

def get_primes(n):
    def temp(values):
        upperBoundSquareRoot = int(n ** 0.5)
        not_primes = set()
        for v in values:
            if v > upperBoundSquareRoot:
                break
            if v not in not_primes:
                not_primes |= set(xrange(v*v, n, v))

        return set(values).difference(not_primes)

    values = [2, 3]
    for x in xrange(6, n, 6):
        values.append(x-1)
        values.append(x+1)

    return temp(values)

limit = 1000000 + 1
primes = sorted(get_primes(limit))

total = 0
for x in xrange(2, limit):
    divisible_primes = filter(lambda y: x % y == 0, 
                              takewhile(lambda z: z <= x,
                                        primes))
    
    functions = cycle((neg, pos))
    v = 0
    for y in xrange(1, len(divisible_primes)+1):
        f = functions.next()
        values = map(lambda z: reduce(mul, z),
                     combinations(divisible_primes, y))
        v += f(sum(map(lambda z: len(xrange(x, limit, z)), values)))
    total += limit - x + v
print total + limit - 2
