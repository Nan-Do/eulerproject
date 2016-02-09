def squared_triangle(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

def unique_squared(limit):
    total = 0
    for a in xrange(1, limit):
        for b in xrange(a+1, limit):
            c = limit - (a + b)
            if c < b: break
            if squared_triangle(a, b, c):
                total += 1
                if total > 1:
                    return False
    return total == 1

#print sum(1 for _ in filter(unique_squared, xrange(1, 1500001)))

total = 0
for x in xrange(1, 1500001):
    if x % 10000 == 0: print x
    if unique_squared(x): total += 1
print total
