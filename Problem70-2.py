from itertools import imap, ifilter, takewhile
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

def phi(n, primes=[]):
    dividing_primes = ifilter(lambda x: n % x == 0, 
                              takewhile(lambda x: x < n, 
                                        primes))
    result = int(n * reduce(lambda x, y: x * y,
                            imap(lambda p: 1 - 1 / float(p), 
                                 dividing_primes)))
    return result

def are_permutation(x1, y1):
    x = str(x1)
    y = str(y1)

    return len(x) == len(y)\
            and sorted(x) == sorted(y)

minimum = 5
value = 0

to_primes = 10000000 
primes = get_primes(to_primes)
primes_set = set(primes)
for x in xrange(9983900, 1000000, -1):
    if x in primes_set:
        continue
    
    t = phi(x, primes)
    if (x % 1000) == 0:
        print x, t
    
    if are_permutation(x, t) and x / float(t) < minimum:
        minimum = x / float(t)
        value = x
        print x, t, minimum
print value, minimum
   

