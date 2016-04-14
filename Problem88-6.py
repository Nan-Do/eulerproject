from itertools import dropwhile, count

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

def factorizations_clousure():
    cache = {}
    def _(n, primes=get_primes(125000)):
        if n in cache:
            return cache[n]
        if n in primes:
            cache[n] = set([(n,)])
            return cache[n]

        # Get divisible primes
        divisible_numbers = []
        for x in xrange(2, int(n/2)+1):
            if (n % x) == 0:
                divisible_numbers.append(x)
        print divisible_numbers

        # Compute the factorizations
        factorizations = set()
        for number in divisible_numbers:
            x = n
            total = 1
            while (x % number) == 0:
                x /= number
                if x == 1: break
                factorizations.add(tuple(sorted(([number] * total) + [x])))
                total += 1
        cache[n] = factorizations
        return factorizations
    return _
factorizations = factorizations_clousure()

def product_sum(n, k):
    # Check if on the compositions meet the criteria
    for answer in factorizations(n):
        l = len(answer)
        if l <= k and sum(answer) + (k - l) == n:
            #print n, k
            #print (1,) * (k - l) + answer
            return True

    return False

#answers = set()
#for k in xrange(2, 12001):
#    if k % 1000 == 0: print k
#    #x = dropwhile(lambda x: not product_sum(x, k), count(start=2)).next()
#    for x in count(start=2):
#        if product_sum(x, k):
#            #print k, x
#            answers.add(x)
#            break
#print sum(answers)
print factorizations(16)
