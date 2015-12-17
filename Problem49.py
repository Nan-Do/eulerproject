from itertools import takewhile, count

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
    if (n == 2) or (n == 1) or\
            (n == 3) or (n == 5):
        return True
    if (n % 2) == 0:
        return False

    k = list(takewhile(lambda x: ((n - 1) % (2 ** x)) == 0, count()))[-1]
    m = (n - 1) / (2 ** k)

    return all(compute_bi(x, m) for x in [2, 3, 5])

def list_to_int(a):
    return sum(map(lambda x: x[0]*(10**x[1]), zip(a, xrange(len(a)-1, -1, -1))))

def chunks(l, n, step=None):
    if not step:
        step = n
    return [l[i:i + n] for i in range(0, len(l)-1, step)]

def mod(n):
    if n < 0:
        return -n
    else:
        return n

def is_permuation(current, element):
    return sorted(str(current)) == sorted(str(element))

primes = filter(is_prime, xrange(1001, 10001, 2))
while len(primes) != 0:
    current = primes.pop()
    answers = []
    for element in primes:
        if is_permuation(current, element):
            primes.remove(element)
            answers.append(element)
    if len(answers) < 3:
        continue
    answers.append(current)
    answers = sorted(answers)
    differences = map(lambda x: mod(x[1] - x[0]), chunks(answers, 2, 1))
    print answers, differences
