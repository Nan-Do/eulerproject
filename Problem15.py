from operator import mul


def Lattice(start, end):
    # Combinatorical solution
    def binomial(n, k):
        a = reduce(mul, xrange(n, k, -1))
        b = reduce(mul, xrange(1, k + 1))

        return a / b

    n = end[0] - start[0]
    k = end[1] - start[1]

    return binomial(n + k, n)


print Lattice((0, 0), (20, 20))
