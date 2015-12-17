import pprint


def is_pythagorean(a, b, c):
    a2 = pow(a, 2)
    b2 = pow(b, 2)
    c2 = pow(c, 2)
    return c2 == (a2 + b2)


def compute_answers(p):
    ans = set()
    for x in xrange(1, p / 2):
        for y in xrange(x, p / 2):
            c = p - (x + y)
            if is_pythagorean(x, y, c):
                ans.add((x, y, c))
    return ans

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(sorted(enumerate(map(compute_answers, xrange(1, 1001)), start=1),
                 cmp=lambda x, y: cmp(len(x[1]), len(y[1])),
                 reverse=True)[0])
