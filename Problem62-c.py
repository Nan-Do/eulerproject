from itertools import count, permutations
from math import ceil

def is_cube(n):
    v = ceil(pow(n, (1/3.)))
    return (v ** 3) == n

def convert_to_int(n):
    y = 0
    for x in xrange(len(n)):
        y = (y * 10) + (ord(n[x]) - 48)
    return y

def check_cube(number, limit):
    count = 0
    repeated = set()
    for n in permutations(str(number)):
        if n[0] == '0' or n in repeated: continue
        repeated.add(n)
        if is_cube(convert_to_int(n)):
            count += 1
        if count == limit:
            return True
    return False

for n in count(start=1002):
    cube = pow(n, 5)
    print n, cube
    if check_cube(cube, 4):
        print n, cube
        break
