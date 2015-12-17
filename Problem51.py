from itertools import takewhile, count, combinations
from sys import exit

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


def substitute_values(number, positions, substitutions):
    results = set()
    number = str(number)
    for value in substitutions:
        n = number
        for position in positions:
            n = n[:position] + str(value) + n[position+1:]
        if int(n) < (10 ** (len(number) - 1)):
            continue
        results.add(int(n))
    return results


for prime in primes:
    b = str(prime)
#    print b
    for n in xrange(1, len(b)):
        substitutions = list(combinations(xrange(len(b)), n))
        for v in map(lambda x: substitute_values(b, x, xrange(0, 10)), substitutions):
            num_primes = filter(lambda x: x in primes_set, v)
#            print "\t", num_primes
            if len(num_primes) == 8:
                print num_primes, sorted(v)[0]
                exit(0)
