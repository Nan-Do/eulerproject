from itertools import imap, ifilter, takewhile, islice
from functools import reduce

def get_primes(n):
    def temp(values):
        upperBoundSquareRoot = int(n ** 0.5)
        primes = list()
        isComposite = [False for _ in xrange(n)]
        for v in values:
            if v > upperBoundSquareRoot:
                break
            if not isComposite[v]:
                primes.append(v)
                for k in xrange(v*v, n, v):
                    isComposite[k] = True
        for m in xrange(upperBoundSquareRoot, n):
            if not isComposite[m]:
                primes.append(m)
        return primes

    values = [2, 3]
    for x in xrange(6, n, 6):
        values.append(x-1)
        values.append(x+1)

    return temp(values)

def are_permutation(x1, y1):
    x = str(x1)
    y = str(y1)

    return len(x) == len(y)\
            and sorted(x) == sorted(y)

minimum = 5
value = 0

count = 0
primes = list(reversed(get_primes(10000)))
for x in primes:
    for y in primes:
        a = x * y
        if a < 4000000 or a > 10000000:
            continue
        t = int(a * (1 - (1/float(x))) * (1 - (1/float(y))))
        if a / float(t) < minimum and are_permutation(a, t):
            value = a
            minimum = a / float(t)

print value, minimum
   

