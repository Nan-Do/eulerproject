def generate_solutions(n):
    solutions = []
    for x in xrange(1, n/2+1):
        solutions.append((n-x, x))
    return solutions

def ways_to_write(n):
    r = {1:1, 2:1, 3:2, 4:4}
    for x in xrange(5, n+1):
        g = generate_solutions(x)
        res = sum(map(lambda y: r[y[0]] * r[y[1]], g))
        r[x] = res
        #print x, res
    return r[n]


print ways_to_write(6)
print ways_to_write(7)
print ways_to_write(8)
print ways_to_write(9)

