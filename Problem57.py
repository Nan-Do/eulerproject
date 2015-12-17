from collections import namedtuple

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

def f(n):
    if n == 1:
        return "1/2"
    else:
        return "1/(2 + " + f(n-1) + ")"

def f2(n):
    if n == 1:
        return Fraction(1, 2)
    else:
        x = f2(n - 1)
        f = add_fractions(Fraction(2, 1), x)
        return Fraction(f.denominator, f.numerator)

def f3(n):
    f = Fraction(1, 2)
    for _ in xrange(n-1):
        f = add_fractions(Fraction(2, 1), f)
        f = Fraction(f.denominator, f.numerator)
    return f

count = 0
for n in xrange(1, 1001):
    f = add_fractions(Fraction(1,1), f3(n))
    if len(str(f.numerator)) > len(str(f.denominator)):
        count += 1
print count
