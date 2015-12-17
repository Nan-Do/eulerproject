from itertools import count

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


primes = get_primes(100000000)

def gen_diagonals(n):
    last = 1
    diagonals = [1]
    for x in xrange(2, n, 2):
        for _ in xrange(4):
            last += x
            diagonals.append(last)

    return diagonals

for x in count(7, 2):
    n_prim = filter(lambda x: x in primes, gen_diagonals(x))
    ratio = len(n_prim) / float((2 * x) - 1)

    print 'Value:', x, 'Ratio:', ratio
    if ratio < 0.1:
        print x
        break
