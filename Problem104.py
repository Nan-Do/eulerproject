from math import log10, floor

def get_number_of_digits(n):
    return long(floor(log10(n))) + 1

def list_of_digits(n):
    r = []
    while n > 9:
        n, x = divmod(n, 10)
        r.append(x)
    r.append(n)
    return r


def fib():
    yield 0; yield 1; yield 1

    a = b = 1
    while True:
        yield a + b
        c = a
        a = a + b
        b = c


f = fib()
f.next()
digits = set(xrange(1, 10))
for pos, value in enumerate(f, start=1):
    n = get_number_of_digits(value)
    d1 = set(list_of_digits(value / 10 ** (n - 9)))
    d2 = set(list_of_digits(value % (10 ** 9)))
    if (d2 == d1) and d1 == digits:
        print pos
        break
