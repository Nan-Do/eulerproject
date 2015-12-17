from math import floor

def gen_values(n):
    m = 0
    d = 1
    a0 = a1 = floor(n ** 0.5)
    while 2 * a0 != a1:
        m =  d * a1 - m
        d = (n - (m ** 2)) / d
        a1 = floor((a0 + m) / d)
        yield a1

def is_not_cube(n):
    x = floor(n ** 0.5)
    return (x * x) != n

total = 0
for n in filter(is_not_cube, xrange(2, 10001)):
    if (len(list(gen_values(n))) % 2) == 1:
        total += 1
print total
