from itertools import product, permutations, combinations
from operator import mul, add, sub, truediv

def compute_value(numbers, operations):
    r = operations[0](numbers[0], numbers[1])
    for x in xrange(1, len(operations)):
        r = operations[x](r, numbers[x+1])
    r2 = operations[1](operations[0](numbers[0], numbers[1]),
                       operations[0](numbers[0], numbers[1]))
    return r, r2

def consecutive_values(values):
    total = 0
    for x in xrange(1, len(values)):
        if values[x] != values[x-1] + 1:
            break
        total += 1
    return total
            

ops = (mul, add, sub, truediv)
maximum_value = 0
result = None
sequence = None
for numbers in combinations(xrange(1, 10), 4):
    results = set()
    for c in permutations(numbers, len(numbers)):
        for operations in product(ops, ops, ops):
            res, res2 = compute_value(c, operations)
            int_res = int(res)
            if res > 0 and int_res == res:
                results.add(int_res)
            int_res = int(res2)
            if res2 > 0 and int_res == res2:
                results.add(int_res)
    s = sorted(results)
    if numbers == (1, 2, 5, 8):
        print numbers, s, consecutive_values(s)
    if s[0] == 1:
        v = consecutive_values(s) 
        if v >= maximum_value:
            result = numbers
            maximum_value = v
            sequence = s
            print result, maximum_value
print result, maximum_value
