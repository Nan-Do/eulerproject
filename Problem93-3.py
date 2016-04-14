from itertools import product, permutations, combinations
from operator import mul, add, sub, div

def compute_value(numbers, operations):
    r = operations[0](numbers[0], numbers[1])
    for x in xrange(1, len(operations)):
        r = operations[x](r, numbers[x+1])
    return r

def consecutive_values(values):
    total = 0
    for x in xrange(1, len(values)):
        if values[x] != values[x-1] + 1:
            break
        total += 1
    return total
            

ops = (mul, add, sub, div)
maximum_value = 0
result = None
#for numbers in combinations(xrange(1, 50), 4):
#    results = set()
#    for c in permutations(numbers, len(numbers)):
#        for operations in permutations(ops, 3):
#            res = compute_value(c, operations)
#            if res > 0:
#                results.add(res)
#    s = sorted(results)
#    if s[0] == 1:
#        v = consecutive_values(s) 
#        if v > maximum_value:
#            result = numbers
#            maximum_value = v
#print result, maximum_value
numbers = (5,6,8,44) + xrange(150, 200)
results = set()
for c in permutations(numbers, len(numbers)):
    for operations in product(ops, ops, ops):
        res = compute_value(c, operations)
        if res > 0:
            results.add(res)
print results, len(results)
