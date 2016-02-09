from itertools import takewhile, count
from collections import deque

def max_min(a, b):
    if a > b:
        return (a, b)
    else:
        return (b, a)

def get_primes(n):
    def temp(values):
        upperBoundSquareRoot = int(n ** 0.5)
        not_primes = set()
        for v in values:
            if v > upperBoundSquareRoot:
                break
            if v not in not_primes:
                not_primes |= set(xrange(v*v, n, v))

        return set(values).difference(not_primes)

    values = [2, 3]
    for x in xrange(6, n, 6):
        values.append(x-1)
        values.append(x+1)

    return temp(values)
primes = get_primes(100000)
primes_list = sorted(primes)

def generate_solutions_decorator():
    cache = {}
    def _(n, primes):
        if n in cache:
            return cache[n]
        p = takewhile(lambda x: x < n, primes)
        solutions = []
        for v in p:
            solution = max_min(n-v, v)
            if solution not in solutions:
                solutions.append(solution)
        cache[n] = solutions
        return solutions
    return _
generate_solutions = generate_solutions_decorator()

def ways_to_write(n):
    total = 0
    queue = deque(generate_solutions(n, primes_list))
    level_solutions = set()
    current_length = 2
    while queue:
        element = queue.popleft()
        if len(element) > current_length:
            level_solutions = set()
            current_length = len(element)
        if all(map(lambda x: x in primes, element)):
            total += 1
        for s in generate_solutions(element[0], primes_list):
            solution = tuple(sorted(s + element[1:], reverse=True))
            if solution in level_solutions:
                continue
            
            level_solutions.add(solution)
            queue.append(solution)

    return total

for x in count(start=2, step=1):
    total = ways_to_write(x)
    print x, total
    if total > 5000:
        print total
        break
