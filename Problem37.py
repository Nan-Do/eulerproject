from itertools import takewhile, count, imap


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
    if (n == 2) or (n == 3) or (n == 5):
        return True
    if (n % 2) == 0 or (n == 1):
        return False

    k = list(takewhile(lambda x: ((n - 1) % (2 ** x)) == 0, count()))[-1]
    m = (n - 1) / (2 ** k)

    return all(compute_bi(x, m) for x in [2, 3, 5])


def truncate_l(n):
    return [n % 10 ** i for i in xrange(len(str(n))-1, 0, -1)]

def truncate_r(n):
    return [n / 10 ** i for i in xrange(1, len(str(n)))]

def check(n):
    return is_prime(n) and all(imap(is_prime, truncate_l(n))) and\
    all(imap(is_prime, truncate_r(n)))

r = []
c = count(start=11)
while len(r) < 11:
    v = c.next()
    if check(v):
        r.append(v)

print sum(r)
