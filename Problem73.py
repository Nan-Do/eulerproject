import fractions 

top = 1 / 2.0
bottom = 1 / 3.0
limit = 12001 
total = 0

for x in xrange(1, limit):
    for y in xrange(x+1, limit):
        value = x / float(y)
        if value <= bottom:
            break
        if value < top and x % y != 0 and fractions.gcd(x, y) == 1:
            total += 1
print total
