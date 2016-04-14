from math import sqrt

def compute_route(a, b, c):
    d = a + b
    return sqrt(c*c + d*d)

def compute_integer_routes(M):
    total = 0
    for x in xrange(1, M+1):
        for y in xrange(x, M+1):
            for z in xrange(y, M+1):
                d = min(compute_route(x, y, z),
                        compute_route(x, z, y),
                        compute_route(z, y, x))

                if d == int(d):
                    #print (x, y, z)
                    total += 1
    return total

#for x in xrange(1500, 2000, 50):
#    print x, compute_integer_routes(x)
for x in xrange(1811, 1820, 1):
    print x, compute_integer_routes(x)
