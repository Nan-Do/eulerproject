from itertools import count

def ways_to_write_generator():
    r = {1:1, 2:1, 3:2, 4:4}
    def generate_solutions(n):
        solutions = []
        for x in xrange(1, n/2+1):
            solutions.append((n-x, x))
        return solutions


    n = 5
    while True:
        g = generate_solutions(n)
        res = sum(map(lambda y: r[y[0]] * r[y[1]], g)) 
        r[n] = res
        yield res + 1
        n += 1

current = 1
for w in ways_to_write_generator():
    print current, w
    current += 1
    if current > 50:
        break
