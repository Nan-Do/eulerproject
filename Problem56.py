def s(a, b):
    return sum(map(int, str(a**b)))

print max([s(a, b) for a in xrange(101) for b in xrange(101)])
