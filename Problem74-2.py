def factorial(n):
    if n == '0' or n == '1': return 1
    elif n == '2': return 2
    elif n == '3': return 6
    elif n == '4': return 24
    elif n == '5': return 120
    elif n == '6': return 720
    elif n == '7': return 5040
    elif n == '8': return 40320
    elif n == '9': return 362880
    else:
        raise ValueError(n)

def compute_number(n):
    res = 0
    for x in str(n):
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
    if cycle_length == 60:
        total += 1
print total
