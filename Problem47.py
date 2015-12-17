from itertools import takewhile, count, islice

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
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

primes = list(islice(gen_primes(), 200))
primes_set = set(primes)

def get_factors(n):
    def get_maximum_exponent(b):
        return list(takewhile(lambda x: (n % (b ** x)) == 0, count(1)))[-1]

    answers = set()
    for x in primes:
        if n % x == 0:
            value = get_maximum_exponent(x)
            answers.add(x ** value)

            n /= (x ** value)
            if n == 1:
                break

    return answers

c = 0
sets = []
numbers = []
for number in count(3, 1):
    if c == 4:
        break
    if number in primes_set:
        sets = []
        numbers = []
        c = 0
        continue
    g = get_factors(number)
    if len(g) >= 4 and all(map(lambda x: x.intersection(g) == set(),
                               sets)):
        c += 1
        sets.append(g)
        numbers.append(number)
    else:
        c = 0
        sets = []
        numbers = []

print numbers, sets
