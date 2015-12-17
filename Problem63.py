for x in xrange(1, 500):
    for n in xrange(1, 500):
        value = pow(x, n)
        if len(str(value)) == n:
            print x, n
