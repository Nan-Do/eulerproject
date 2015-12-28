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
    def gcd(num1, num2):
        tmp = 0
        num1 = abs(num1)
        num2 = abs(num2)
        while (num1 > 0):
            tmp = num1
            num1 = num2 % num1
            num2 = tmp
        return num2

    if n in primes:
        return n - 1
    else:
        count = 1
        for x in xrange(2, n):
            if gcd(x, n) == 1:
               count += 1
        return count

m = n = 0
for x in xrange(2, 1000001):
    if (x % 10000) == 0: print x, m, n
    temp = (x / float(totient(x)))
    if temp > m:
        m = temp
        n = x
print n, m
