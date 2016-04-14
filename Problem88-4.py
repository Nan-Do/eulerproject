from operator import mul
from itertools import takewhile, dropwhile, count, repeat, combinations


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

def get_divisible_primes(n, primes=get_primes(150)):
    top = (n / 2) + 1
    divisible = filter(lambda x: (n % x) == 0, 
                       takewhile(lambda x: x <= top, primes))
    return list(divisible)

def product_sum(n, k):
    primes = get_divisible_primes(n)
    if len(primes) > k:
        return None
    
    # Obtain the composition of the number in terms of its primes
    primes_composition = []
    for prime in primes:
        current = prime
        total = 0
        while (n % current) == 0:
            current *= prime
            total += 1
        
        primes_composition.extend(repeat(prime, total))

    # Get all the other compositions
    answers = set()
    answers.add(tuple(primes_composition))
    for x in xrange(2, len(primes_composition)):
        for comb in set(combinations(primes_composition, x)):
            p = primes_composition[:]
            for element in comb:
                p.remove(element)
            answers.add(tuple(sorted([reduce(mul, p)] +
                                     [reduce(mul, comb)])))
            answers.add(tuple(sorted(p + [reduce(mul, comb)])))

    # Check if on the compositions meet the criteria
    for answer in sorted(answers):
        l = len(answer)
        if l <= k and sum(answer) + (k - l) == n:
            #print (1,) * (k - l) + answer 
            return True

    return False

#for x in xrange(15):
#    print x, product_sum(x, 10)

answers = set()
for k in xrange(2, 120001):
    if k % 100 == 0: print k
    x = dropwhile(lambda x: not product_sum(x, k), count(start=2)).next()
    answers.add(x)

print sum(answers)
#print product_sum(12, 6)
#print product_sum(16, 10)
