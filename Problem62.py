from itertools import count, permutations
from math import ceil

def gen_cubes():
    for n in count(start=1):
        yield n ** 3

def is_cube(n):
    v = ceil(pow(n, (1/3.)))
    return (v ** 3) == n

def check_cube(number, limit):
    n_str = str(number)
    count = 0
    for n in map(lambda x: int("".join(x)), set(permutations(n_str))):
        if len(str(n)) != len(n_str):
            continue
        if is_cube(n):
            count += 1
        if count == limit:
            return True
    return False

for n in gen_cubes():
    if check_cube(n, 4):
        print n
        break
