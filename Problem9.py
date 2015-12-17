from itertools import count

pyt = ((a, b, c)
       for a in xrange(1, 500)
       for b in xrange(1, 500)
       for c in xrange(1, 500)
       if ((a**2 + b**2) == c**2))


for a,b,c in pyt:
    if (a + b + c) == 1000:
        print a*b*c
        break
