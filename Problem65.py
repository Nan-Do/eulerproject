from collections import namedtuple
from math import floor, exp, ceil
from itertools import cycle

Fraction = namedtuple('Fraction', ['numerator', 'denominator'], verbose=False)

def abs(num):
    if num < 0:
        return -num
    return num

def gcd(num1, num2):
    tmp = 0
    num1 = abs(num1)
    num2 = abs(num2)
    while (num1 > 0):
        tmp = num1
        num1 = num2 % num1
        num2 = tmp
    return num2

def reduce(numerator, denominator):
    g = gcd(numerator, denominator)
    return Fraction(numerator/g, denominator/g)

def add_fractions(f1, f2):
   denominator = f1.denominator * f2.denominator
   numerator = f1.numerator * (denominator / f1.denominator) +\
               f2.numerator * (denominator / f2.denominator)
   return reduce(numerator, denominator)

def f3(n, values):
    x = reversed(values)
    f = Fraction(1, x.next())
    for _ in xrange(n-1):
        f = add_fractions(Fraction(x.next(), 1), f)
        f = Fraction(f.denominator, f.numerator)
    return f


n = 100
v  = gen_values(exp(1))
values = []
for p in xrange(1, int(ceil(n/3.))):
    values.append(1)
    values.append(2*p)
    values.append(1)
    

print values
f = add_fractions(Fraction(2, 1), f3(n-1, values))
print sum(map(int, str(f.numerator)))

