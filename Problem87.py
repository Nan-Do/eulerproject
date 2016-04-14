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

    return sorted(temp(values))

def compute_value(n):
    primes = get_primes(int(n**0.5+1))
    numbers = set()
    for x in map(lambda r: r ** 2, primes):
        if x >= n: break
        for y in map(lambda r: r ** 3, primes):
            if (x + y) >= n: break
            for z in map(lambda r: r ** 4, primes):
                if (x + y + z) < n:
                    #print x + y + z
                    numbers.add(x + y + z)
                else: break

    return len(numbers)

print compute_value(50000000)
