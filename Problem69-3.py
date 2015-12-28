import fractions

mul_2 = set(xrange(2, 1000001, 2))
mul_3 = set(xrange(3, 1000001, 3))
mul_5 = set(xrange(5, 1000001, 5))
values = mul_2.intersection(mul_3.intersection(mul_5))

def totient(n):
    count = 1
    for x in xrange(2, n):
        if fractions.gcd(x, n) == 1:
            count += 1
    return count

m = n = 0
for pos,x in enumerate(values):
    if (pos % 5000) == 0: print x, n, m
    temp = (x / float(totient(x)))
    if temp > m:
        m = temp
        n = x
print n, m
