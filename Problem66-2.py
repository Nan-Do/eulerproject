from itertools import count
from math import ceil

def function_y(x, D):
    return (((x ** 2) - 1) / float(D)) ** 0.5

def function_x(y, D):
    return ((D * (y * y)) + 1) ** 0.5

def is_int(x):
    return (ceil(x) == x)

def is_cube(n):
    v = ceil(pow(n, 0.5))
    return (v ** 2) == n

max_x = -1
RD = 0
for D in xrange(1001, 700, -1):
    if is_cube(D):
        continue
    for x in count(start=2):
        y = function_y(x, D)
        if is_int(y):
            if x > max_x:
                max_x = x
                RD = D
            print "For D:", D, "X:", x, "Y:", y
            break

print "Max X", max_x, "D", RD
