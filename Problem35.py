from itertools import takewhile, count


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
    if (n == 1) or (n == 2) or\
            (n == 3) or (n == 5):
        return True
    if (n % 2) == 0:
        return False

    k = list(takewhile(lambda x: ((n - 1) % (2 ** x)) == 0, count()))[-1]
    m = (n - 1) / (2 ** k)

    return all(compute_bi(x, m) for x in [2, 3, 5])


def round_robin(n):
    def get_digits(r):
        digits = []
        while (r > 9):
            digits.append(r % 10)
            r /= 10
        digits.append(r)
        return digits

    digits = get_digits(n)
    for x in xrange(len(digits)):
        number = sum(map(lambda x: (10 ** x[0]) * x[1],
                         enumerate(digits[x:] + digits[:x])))
        yield number


def all_round_prime(n):
    return all(map(is_prime, round_robin(n)))

print len(filter(all_round_prime, xrange(2, 1000001)))
