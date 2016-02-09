from fractions import Fraction

def gen_triplets_Plato(limit):
    odd = 3
    for x in xrange(1, limit+1):
        f = x + Fraction(x, odd)
        a = f.denominator
        b = f.numerator
        c = int((a ** 2 + b ** 2) ** 0.5)
        yield (a, b, c)
        odd += 2

def gen_triplets_Pythagoras(limit):
    for n in xrange(1, limit+1):
        _4n = 4 * n
        f = n + Fraction(_4n+3, _4n+4)
        a = f.numerator
        b = f.denominator
        c = int((a ** 2 + b ** 2) ** 0.5)
        yield (a, b, c)


limit = 100
plato = gen_triplets_Plato(limit)
pytha = gen_triplets_Pythagoras(limit)
for _ in xrange(limit):
    x = plato.next()
    if x[2] < 100:
        print x, sum(x)

    x = pytha.next()
    if x[2] < 100:
        print x, sum(x)

