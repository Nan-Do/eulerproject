from itertools import permutations, dropwhile

c = dropwhile(lambda x: x[0] != 1000000,
              enumerate(permutations(xrange(10)),
                        start=1)).next()

print "".join(map(str, c[1]))
