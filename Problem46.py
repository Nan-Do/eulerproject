from itertools import takewhile, imap, count, islice

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

def gen_primes():
    n = 1
    while True:
        if is_prime(n):
            yield n
        n += 1

def twice_squares():
    return imap(lambda x: 2 * x * x, count(1))


def goldbachs(n, primes, twice_squares):
    for x in primes:
        if x > n:
            return None
        for y in twice_squares:
            if x + y == n:
                return [True, x, y]

    None


primes = list(islice(gen_primes(), 1000))
primes_set = set(primes)
twice_squares = list(islice(twice_squares(), 10000))


for x in xrange(1, 10001, 2):
    if x in primes_set: continue
    if goldbachs(x, primes, twice_squares) == None:
        print "Value: ", x
        break
