from math import floor
from fractions import Fraction
from itertools import islice, count

def gen_values(n):
    m = 0
    d = 1
    a0 = a1 = floor(n ** 0.5)
    yield int(a0)
    while 1:
        m = d * a1 - m
        d = (n - (m ** 2)) / d
        a1 = floor((a0 + m) / d)
        yield int(a1)

def compute_fractions(values):
    x = reversed(list(values))
    f = Fraction(1, int(x.next()))
    for value in x:
        f = Fraction(int(value), 1) + f
        f = Fraction(f.denominator, f.numerator)
    return f.denominator, f.numerator

def is_not_cube(n):
    x = floor(n ** 0.5)
    return (x * x) != n

def compute_fraction_digits(f):
    a = f[0]; b = f[1]
    while True:
        (res, a) = divmod(a, b)
        yield res
        a *= 10
        while a < b:
            a *= 10
            yield 0

total = 0
for x in filter(is_not_cube, xrange(1, 101)):
    f = compute_fractions(islice(gen_values(x), 250))
    total += sum(list(islice(compute_fraction_digits(f), 100)))
print total
