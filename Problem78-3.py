from itertools import count, product, chain

def max_min(a, b):
    if a > b:
        return (a, b)
    else:
        return (b, a)

def ways_to_write_generator():
    r = {1:[(1,)], 2:[(2,), (1, 1)]}
    def generate_solutions(n):
        solutions = []
        for x in xrange(1, n/2+1):
            solutions.append(max_min(n-x, x))
        return solutions

    n = 3
    while True:
        answers = set()
        for g in generate_solutions(n):
            answers.add(g)
            for c in product(r[g[0]], r[g[1]]): 
                s = tuple(sorted(chain.from_iterable(c), reverse=True))
                answers.add(s)
        yield answers
        r[n] = answers
        n += 1

c = 3
for x in  ways_to_write_generator():
    print c, len(x)
    if c == 15:
        break
    c += 1
