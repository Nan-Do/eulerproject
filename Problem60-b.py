from itertools import combinations

a = [(3, 7, 109, 673),
     (3, 7, 2503, 9601),
     (3, 7, 541, 4159),
     (3, 7, 4729, 9601),
     (3, 11, 2069, 2297),
     (3, 11, 2069, 8747),
     (3, 11, 2069, 8219),
     (3, 11, 23, 8747),
     (3, 11, 8747, 701),
     (3, 17, 2069, 2297),
     (3, 17, 2069, 449),
     (3, 17, 6353, 449),
     (3, 17, 449, 6599),
     (3, 2069, 191, 8747),
     (3, 31, 8431, 7591),
     (3, 31, 1237, 6571),
     (3, 37, 67, 2377),
     (3, 37, 67, 5923),
     (3, 37, 2377, 4159),
     (3, 37, 4729, 7963),
     (3, 37, 1237, 8713),
     (3, 37, 8713, 1699),
     (3, 37, 7963, 5923),
     (3, 61, 331, 3637),
     (3, 61, 6871, 3637),
     (3, 61, 7963, 9181),
     (3, 73, 6793, 7159),
     (3, 331, 8431, 739),
     (3, 2503, 5281, 5869),
     (3, 467, 617, 4253),
     (3, 4729, 1051, 9601),
     (3, 4729, 7963, 9181),
     (3, 4919, 8783, 3923),
     (3, 1237, 8713, 6571),
     (3, 8713, 6571, 1699),
     (7, 19, 97, 4507),
     (7, 19, 97, 3727),
     (7, 19, 1249, 3727),
     (7, 19, 3727, 5659),
     (7, 61, 487, 8941),
     (7, 61, 3181, 1693),
     (7, 4219, 2089, 3181),
     (7, 127, 7723, 6949),
     (7, 2269, 853, 8779),
     (7, 2269, 3613, 5821),
     (7, 2089, 2953, 3181),
     (7, 4441, 6949, 1249),
     (7, 2467, 541, 8167),
     (7, 433, 1471, 3613),
     (7, 433, 3613, 9613),
     (7, 2671, 829, 3361),
     (7, 6949, 1249, 3727),
     (7, 853, 8017, 8779),
     (7, 1237, 1549, 3019),
     (7, 9613, 3019, 7351),
     (11, 23, 6329, 7331),
     (11, 23, 5849, 8681),
     (11, 23, 8747, 3083),
     (11, 23, 743, 1871),
     (11, 23, 8681, 1871),
     (11, 23, 1871, 8171),
     (11, 5807, 6329, 1103),
     (11, 5807, 239, 3467),
     (11, 239, 1049, 1847),
     (11, 239, 1091, 1847),
     (11, 2297, 7127, 4967),
     (11, 5849, 353, 4967),
     (11, 5849, 5153, 4643),
     (11, 353, 8831, 6791),
     (11, 353, 8219, 4967),
     (11, 4547, 8831, 6791),
     (11, 8747, 701, 7541),
     (11, 5153, 4643, 4013),
     (13, 19, 5077, 6043),
     (13, 19, 6991, 9697),
     (13, 8389, 6733, 5197),
     (13, 8389, 6733, 5701),
     (13, 8389, 5197, 5701),
     (13, 61, 2383, 5431),
     (13, 127, 6733, 7993),
     (13, 8461, 4363, 9091),
     (13, 9883, 4327, 4591),
     (13, 2383, 8599, 6733),
     (13, 2383, 8599, 5431),
     (13, 6733, 5197, 5701),
     (13, 6343, 4951, 9697),
     (13, 2851, 4951, 9697),
     (13, 1543, 8053, 3967),
     (2063, 47, 9239, 6599),
     (2063, 2243, 6599, 5477),
     (17, 6353, 449, 9923),
     (17, 8537, 4649, 2741),
     (17, 6899, 2741, 3917),
     (17, 4649, 2741, 3917),
     (19, 31, 181, 9679),
     (19, 31, 6271, 1237),
     (19, 31, 6271, 8641),
     (19, 31, 991, 8641),
     (19, 3847, 8929, 5737),
     (19, 6961, 8623, 3727),
     (19, 6991, 9403, 9697),
     (23, 8237, 2357, 6323),
     (23, 47, 4211, 5483),
     (23, 47, 4211, 1481),
     (23, 47, 2333, 5927),
     (23, 89, 2357, 6323)]


def get_primes(n):
    def temp(values):
        upperBoundSquareRoot = int(n ** 0.5)
        primes = set()
        isComposite = [False for _ in xrange(n)]
        for v in values:
            if v > upperBoundSquareRoot:
                break
            if not isComposite[v]:
                primes.add(v)
                for k in xrange(v*v, n, v):
                    isComposite[k] = True
        for m in xrange(upperBoundSquareRoot, n):
            if not isComposite[m]:
                primes.add(m)
        return primes

    values = [2, 3]
    for x in xrange(6, n, 6):
        values.append(x-1)
        values.append(x+1)

    return temp(values)

def gen_is_prime(size):
    primes_buffer = get_primes(size)
    def _(n):
        if n in primes_buffer:
            return True
        if (n % 2) == 0:
            return False
        for x in xrange(3, int(n**0.5), 2):
            if (n % x) == 0:
                return False
        return True
    return _
is_prime = gen_is_prime(120000)

def check_combinations(combination):
    for c in combinations(combination, 2):
        a = str(c[0]) + str(c[1])
        b = str(c[1]) + str(c[0])
        if not is_prime(int(a)) or not is_prime(int(b)):
            return False
    return True


def gen_combinations(numbers, length=3):
    for c in combinations(numbers, length):
        yield c


for element in a:
    for p in get_primes(15000):
        if p not in element and check_combinations([p] + list(element)):
            print sum([p] + list(element))

