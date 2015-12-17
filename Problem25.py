from __future__ import division
from itertools import dropwhile

v = 10 ** 999


def fib():
    a = 0
    b = 1
    while True:
        yield a + b
        temp = a + b
        a = b
        b = temp

c = dropwhile(lambda x: (x[1] / v) < 1.0,
              enumerate(fib(), start=1)).next()

print c[0] + 1
