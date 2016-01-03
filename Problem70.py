from itertools import dropwhile
import fractions

def get_primes(n):
    def temp(values):
        upperBoundSquareRoot = int(n ** 0.5)
        primes = list()
        isComposite = [False for _ in xrange(n)]
        for v in values:
            if v > upperBoundSquareRoot:
                break
            if not isComposite[v]:
                primes.append(v)
                for k in xrange(v*v, n, v):
                    isComposite[k] = True
        for m in xrange(upperBoundSquareRoot, n):
            if not isComposite[m]:
                primes.append(m)
        return primes

    values = [2, 3]
    for x in xrange(6, n, 6):
        values.append(x-1)
        values.append(x+1)

    return temp(values)

def totient(n):
    count = 1
    for x in xrange(2, n):
        if fractions.gcd(x, n) == 1:
            count += 1
    return count

def are_permutation(x1, y1):
    x = str(x1)
    y = str(y1)

    return len(x) == len(y)\
            and sorted(x) == sorted(y)

minimum = 5
value = 0
# for x in map(lambda x: x*x, get_primes(3163)):
#     t = totient(x)
#     if are_permutation(x, t) and x / float(t) < minimum:
#         minimum = x / float(t)
#         value = x
#         print x, t, minimum
# print value, minimum
#


first_prime = 7
to_primes = 10000000 / first_prime
for pos, x in enumerate(reversed(map(lambda x: first_prime * x, 
                                     get_primes(to_primes)))):
    if pos % 100 == 0:
        print pos, x
    t = totient(x)
    if are_permutation(x, t) and x / float(t) < minimum:
        minimum = x / float(t)
        value = x
        print x, t, minimum
print value, minimum
   

