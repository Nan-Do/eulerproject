def compute_terms(a, b):
    return set(i ** j for i in xrange(2, a+1)
                      for j in xrange(2, b+1))

print len(compute_terms(100, 100))
