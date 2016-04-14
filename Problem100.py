from itertools import count
from fractions import Fraction
from math import ceil

f = Fraction(1, 2)

for x in count(start=1000000000000):
    a = int(ceil(x * 0.7))
    b = a - 1
    c = x
    d = x - 1
    while True:
        v = Fraction(a, c)
        w = Fraction(b, d)
        s = v * w
        if s == f:
            print a, x-a, x
            break
        elif s > f:
            break
        a += 1; b += 1


