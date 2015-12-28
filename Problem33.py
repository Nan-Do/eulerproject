from fractions import Fraction 
def compute_new_values(x, y):
    if (x % 10) == (y / 10):
        if (y % 10) == 0:
            return 1, 1
        return x / 10, y % 10
    return 1, 1

f = Fraction(1, 1)
for x in xrange(10, 100):
    for y in xrange(10, 100):
        a, b = compute_new_values(x, y)
        if a != b and (x / float(y)) == (a / float(b)):
            print x, '/', y, ' => ', a,  '/', b
            f *= Fraction(a, b) 
print f.denominator
