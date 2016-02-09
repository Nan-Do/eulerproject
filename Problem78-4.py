def initialize(ways):
    for i in xrange(1, len(ways)):
        for j in xrange(i, len(ways)):
            ways[j] += ways[j-i]

def coins_generator():
    solutions = [1] + [0] * 2
    while 1:
        for i in xrange(1, len(solutions)):
            for j in xrange(i, len(solutions)):
                solutions[j] += solutions[j-i]
        yield solutions[-1]
        solutions.append(0)
        for x in xrange(1, len(solutions)):
            solutions[x] = 0

N = 60000
found = False
while True:
    ways = [1] + [0] * N
    initialize(ways)
    for p, x in enumerate(ways, start=0):
        if x % 1000000 == 0:
            print p, x
            found = True
            break
    if found: break
    N *= 2
    print "Duplicando", N
