from collections import namedtuple

Fraction = namedtuple('Fraction', ['numerator', 'denominator'])

def gen_triplets_fractions(limit):
    def gen_triple(f1, f2):
        f1_b = Fraction(f1.numerator + f1.denominator * 2, f1.denominator)
        f2_b = Fraction(f2.numerator + f2.denominator * 2, f2.denominator)

        a = f1_b.numerator * f2_b.denominator
        b = f1_b.denominator * f2_b.numerator
        c = int((a ** 2 + b ** 2) ** 0.5)
        return (a,b,c)

    yield (3, 4, 5)

    for x in xrange(2, limit+1):
        f1 = Fraction(1, x)
        f2 = Fraction(x * 2, 1)
        yield gen_triple(f1, f2)

        f1 = Fraction(x, x)
        f2 = Fraction(2, 1)
        yield gen_triple(f1, f2)

        f1 = Fraction(2, x+1)
        f2 = Fraction(x+1, 1)
        yield gen_triple(f1, f2)

        f1 = Fraction(2*x, 3)
        f2 = Fraction(3, x)
        yield gen_triple(f1, f2)

g = gen_triplets_fractions(100)
triplets = set()
for t in g:
    a = tuple(sorted(t))
    if a[2] < 100:
        print a

