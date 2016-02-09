def triplet(m, n):
    m2 = m ** 2
    n2 = n ** 2
    return (m2 - n2, 2 * m * n, m2 + n2)
    
for n in xrange(1, 10):
    for m in xrange(n+1, 10):
        a = triplet(m, n)
        print a, sum(a)
