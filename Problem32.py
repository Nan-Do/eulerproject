def compute_mult(a, b):
    res_str = str(a) + str(b) + str(a * b)

    if len(res_str) < 9:
        return -1
    elif len(res_str) > 9:
        return 1
    elif (len(set(res_str)) == 9) and ('0' not in res_str):
        return 0

total = 0
sums = set()
for x in xrange(5000):
    for y in xrange(5000):
        res = compute_mult(x, y)
        if res == 0 and (x * y) not in sums:
            sums.add(x * y)
            total += (x * y)
        elif res == 1:
            break

print total 
