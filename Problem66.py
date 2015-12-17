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

max_x = 0
d = 0
for n in filter(is_not_cube, xrange(2, 1001)):
    for x in count(start=2):
        values = islice(gen_values(n), x)
        x, y = compute_fractions(values)
        if ((x ** 2) - (n * (y ** 2))) == 1:
            if x > max_x:
                max_x = x
                d = n
            break
print d, max_x
