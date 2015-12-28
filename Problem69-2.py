import fractions

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
primes = get_primes(1000000)

def totient(n):
    if n in primes:
        return n - 1
    else:
        count = 1
        for x in xrange(2, n):
            if fractions.gcd(x, n) == 1:
               count += 1
        return count

m = n = 0
for x in xrange(310000, 1000001):
    if (x % 10000) == 0: print x, n, m
    temp = (x / float(totient(x)))
    if temp > m:
        m = temp
        n = x
print n, m
