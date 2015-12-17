from itertools import permutations
from math import ceil

def is_cube(n):
    v = ceil(pow(n, (1/3.)))
    return (v ** 3) == n

def check_cube(number, limit):
    n_str = str(number)
    count = 0
    repeated = set()
    for n in permutations(n_str):
        if n[0] == '0' or n in repeated:
            continue
        if is_cube(int(''.join(n))):
            print '\t\t', n
            repeated.add(n)
            count += 1
        if count == limit:
            return True
    return False

n = 4682
while True:
    value = n ** 3
    print n, value
    if check_cube(value, 5):
        #print n
        break
    n += 1
