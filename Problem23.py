from itertools import count, takewhile, imap


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
    if n in [1, 2, 3, 5]:
        return True
    if (n % 2) == 0:
        return False

    k = list(takewhile(lambda x: ((n - 1) % (2 ** x)) == 0, count()))[-1]
    m = (n - 1) / (2 ** k)

    return all(compute_bi(x, m) for x in [2, 3, 5])


primes = set(x for x in xrange(1, 1000) if is_prime(x))


def number_of_divisors(x):
    divisors = filter(lambda i: (x % i) == 0, primes)
    res = set(divisors)
    current = 0
    while True:
        if current == len(divisors):
            break
        value = divisors[current]
        new_values = set(i * value for i in divisors
                         if (x % (value * i)) == 0)
        if not new_values.issubset(res):
            current = 1
            divisors.extend(sorted(new_values.difference(res)))
            res.update(new_values)
        else:
            current += 1
    res.add(x)
    return res

abundant = [x for x in xrange(2, 14061) if sum(number_of_divisors(x)) > x]
print sum(abundant)
