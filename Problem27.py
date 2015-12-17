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
    if (n == 2) or (n == 1) or\
            (n == 3) or (n == 5):
        return True
    if (n % 2) == 0:
        return False

    k = list(takewhile(lambda x: ((n - 1) % (2 ** x)) == 0, count()))[-1]
    m = (n - 1) / (2 ** k)

    return all(compute_bi(x, m) for x in [2,3,5])


def mod(n):
    if n < 0: return -n
    return n

def gen_function(a, b):
    def f(n):
        return n ** 2 + a * n + b
    return f


m = 0
res = (0, 0)
for a in xrange(-1000, 1001):
    for b in xrange(1, 1001):
        f = gen_function(a, b)
        c = 0
        while is_prime(mod(f(c))): c +=1
        if c > m:
            m = c
            res =(a, b)

print res

