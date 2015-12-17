from operator import mul

def comb(n, r):
    if n == r:
        return 1
    return reduce(mul, xrange(n, n - r, -1)) /\
        reduce(mul, xrange(r, 1, -1))

# count = 0
# for i in xrange(23, 101):
#     for j in xrange(2, i):
#         if comb(i, j) > 1000000:
#             print "C(" + str(i) + ", " + str(j) + ")" + " = " + str(comb(i, j))
#             count += 1
#
# print count


print len(filter(lambda x: comb(x[0], x[1]) > 1000000,
                 [(i, j) for i in xrange(23, 101)
                         for j in xrange(2, i)]))
