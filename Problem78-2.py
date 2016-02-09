from collections import deque

def ways_to_write(x):
    def generate_solutions_decorator():
        cache = {}
        def _(n):
            if n in cache: 
                return cache[n]
            solutions = []
            for x in xrange(1, n/2+1):
                solutions.append((n-x, x))
            cache[n] = solutions
            return cache[n]
        return _
    generate_solutions = generate_solutions_decorator()

    solutions_queue = deque(generate_solutions(x))
    level_solutions = set()
    total_solutions = 0
    current_length = 2
    while solutions_queue:
        current = solutions_queue.popleft()
        if len(current) > current_length:
            #print current_length
            level_solutions = set()
            current_length = len(current)
        total_solutions += 1
        if current[0] == 1: 
            continue
        for solution in generate_solutions(current[0]):
            s = tuple(sorted(solution + current[1:], reverse=True))
            if s in level_solutions:
                continue
            level_solutions.add(s)
            solutions_queue.append(s)
    return total_solutions 

for x in xrange(1, 15):
    print x, ways_to_write(x)
