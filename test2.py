from itertools import permutations, takewhile, count

def is_prime(n):
    def compute_bi(a, m):
        b = pow(a, m, n)
        if b == 1 or b == (n - 1):
            return True

        old_b = set()
        while True:
            b = pow(b, 2, n)
            if (b == 1) or (b in old_b):
                return False
            if (b == (n - 1)):
                return True
            old_b.add(b)
    if n in [1, 2, 3, 5]:
        return True
    if (n % 2) == 0:
        return False

    k = list(takewhile(lambda x: ((n - 1) % (2 ** x)) == 0, count()))[-1]
    m = (n - 1) / (2 ** k)

    return all(compute_bi(x, m) for x in [2, 3, 5])

def list_to_int(a):
    return sum(map(lambda x: x[0]*(10**x[1]), zip(a, xrange(len(a)-1, -1, -1))))

for x in xrange(8, 4, -1):
    for perm in permutations(xrange(x, 0, -1), x):
        a = list_to_int(perm)
        if is_prime(a):
            print a
            break
    if is_prime(a): break

print "No number"
