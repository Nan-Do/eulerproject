from itertools import takewhile, dropwhile, count

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
    top = n / 2
    divisible = filter(lambda x: (n % x) == 0, 
                       takewhile(lambda x: x <= top, primes))
    return list(divisible)


def product_sum(n, k):
    primes = get_divisible_primes(n)
    if len(primes) > k:
        return None
    
    answers = set()
    for prime in primes:
        current = prime
        total = 0
        while (n % current) == 0:
            current *= prime
            total += 1
        
        while total != 0:
            result = [prime] * total
            r = n / (prime * total)
            if r != 1:
                result.append(r)
            answers.add(tuple(sorted(result)))
            total -= 1

        print answers
        for answer in sorted(answers):
            l = len(answer)
            if l <= k and sum(answer) + (k - l) == n:
                #print (1,) * (k - l) + answer 
                return True

    return False

#for x in xrange(15):
#    print x, product_sum(x, 10)

#answers = set()
#for k in xrange(2, 13):
#    x = dropwhile(lambda x: not product_sum(x, k), count(start=2)).next()
#    answers.add(x)
#    print k, x 

#print sum(answers)
print product_sum(16, 10)
