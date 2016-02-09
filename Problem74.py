from math import factorial

def get_digits(n):
    value = n 
    while value> 10:
        value, digit = divmod(value, 10)
        yield digit
    yield value

def compute_number(n):
    res = 0
    for x in get_digits(n):
        res += factorial(x)
    return res

total = 0
for x in xrange(1, 1000000):
    values = set()
    cycle_length = 0
    v = x
    while v not in values:
        values.add(v)
        v = compute_number(v)
        cycle_length += 1
    if cycle_length == 61:
        print x
        total += 1
print total
