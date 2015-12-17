from itertools import takewhile, count

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
    if (n == 2) or (n == 1) or\
            (n == 3) or (n == 5):
        return True
    if (n % 2) == 0:
        return False

    k = list(takewhile(lambda x: ((n - 1) % (2 ** x)) == 0, count()))[-1]
    m = (n - 1) / (2 ** k)

    return all(compute_bi(x, m) for x in [2, 3, 5])

primes = [2] + filter(is_prime,
                      xrange(3, 1000, 2))
primes_set = set(primes)
for i in xrange(1001, 1000000, 2):
    is_prime = True
    for j in primes_set:
        if (i % j) == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

primes_set = set(primes)
print "Primes less than a million computed:", len(primes), len(primes_set)

longest = 0
orig = end = 0
analyzed = 0
for i in xrange(0, len(primes)):
    if primes[i] > 500000:
        break
    for j in xrange(i+1, i+1000):
        if sum(primes[i:j]) in primes_set:
            if (j - i) > longest:
                orig = i
                end = j
                longest = j - i
                print longest, sum(primes[orig:end])
    analyzed += 1

print longest, sum(primes[orig:end])
